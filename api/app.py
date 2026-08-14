from fastapi import FastAPI, HTTPException

from api.schemas import FinancialProfileRequest
from api.service import analyze_financial_profile


# =========================================================
# MONEYBUDDY API
# =========================================================

app = FastAPI(
    title="MoneyBuddy AI API",
    description="AI-powered personal financial intelligence engine",
    version="1.0.0"
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
# FINANCIAL ANALYSIS
# =========================================================

@app.post("/api/v1/analyze")
def analyze(
    request: FinancialProfileRequest
):
    try:

        result = analyze_financial_profile(
            request
        )

        return result

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )