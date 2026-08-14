import json
from pathlib import Path


def load_knowledge_base():

    file_path = Path(__file__).parent / "knowledge_base.json"

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)