from fastapi import FastAPI, HTTPException

from api.schemas import FinancialProfileRequest
from api.service import analyze_financial_profile
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="MoneyBuddy AI API",
    description="AI-powered personal financial intelligence API",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================================================
# HEALTH CHECK
# =========================================================

@app.get("/health")
def health_check():

    return {
        "status": "ok",
        "service": "MoneyBuddy AI"
    }


# =========================================================
# MAIN FINANCIAL ANALYSIS
# =========================================================

@app.post("/api/v1/analyze")
def analyze(
    request: FinancialProfileRequest
):

    try:

        # The service already:
        #
        # 1. Builds the internal profile
        # 2. Runs MoneyBuddy
        # 3. Converts the engine result
        # 4. Validates against MoneyBuddyResponse
        #
        # Therefore DO NOT call build_api_response()
        # again here.

        return analyze_financial_profile(
            request
        )

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )