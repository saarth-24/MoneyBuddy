import os
import json
import time

from dotenv import load_dotenv
from google import genai
from google.genai import errors


load_dotenv()


class AICFOClient:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY is not set in .env"
            )

        self.client = genai.Client(
            api_key=api_key
        )

        # Primary and fallback models to ensure high availability
        self.models = [
            "gemini-2.5-flash",
            "gemini-2.0-flash",
            "gemini-1.5-flash",
            "gemini-3.6-flash"
        ]

    def generate_advice(
        self,
        system_prompt: str,
        user_prompt: str
    ) -> dict:

        prompt = f"""
SYSTEM INSTRUCTIONS:

{system_prompt}

USER FINANCIAL CONTEXT:

{user_prompt}
"""

        last_exception = None

        for model_name in self.models:
            max_retries = 3
            backoff = 2.0

            for attempt in range(max_retries):
                try:
                    response = self.client.models.generate_content(
                        model=model_name,
                        contents=prompt
                    )

                    if not response.text:
                        raise RuntimeError(
                            "Gemini returned an empty response."
                        )

                    raw_text = response.text.strip()

                    # Strip code block markup if present
                    if raw_text.startswith("```"):
                        lines = raw_text.splitlines()
                        if lines[0].startswith("```"):
                            lines = lines[1:]
                        if lines and lines[-1].startswith("```"):
                            lines = lines[:-1]
                        raw_text = "\n".join(lines).strip()

                    try:
                        data = json.loads(raw_text)
                        return data
                    except json.JSONDecodeError as error:
                        raise RuntimeError(
                            "Gemini did not return valid JSON.\n\n"
                            f"Gemini response:\n{raw_text}"
                        ) from error

                except Exception as err:
                    last_exception = err
                    err_msg = str(err)
                    is_transient = (
                        "503" in err_msg
                        or "UNAVAILABLE" in err_msg
                        or "429" in err_msg
                        or "RESOURCE_EXHAUSTED" in err_msg
                    )

                    if is_transient and attempt < max_retries - 1:
                        time.sleep(backoff)
                        backoff *= 2.0
                        continue

                    # If not transient or out of retries on this model, try next model
                    break

        raise RuntimeError(
            f"Failed to generate advice from Gemini models. Last error: {last_exception}"
        ) from last_exception