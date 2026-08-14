from api.schemas import FinancialProfileRequest
from api.adapter import build_financial_profile
from user_profile.adapter import profile_to_user
from api.response_schema import MoneyBuddyResponse
from api.response import build_api_response

from main import run_moneybuddy


def analyze_financial_profile(
    request: FinancialProfileRequest
):
    """
    Main MoneyBuddy API service.

    Backend calls this function with validated
    user information.

    This function runs the complete MoneyBuddy
    financial intelligence pipeline.
    """

    # =====================================================
    # 1. API REQUEST → INTERNAL PROFILE
    # =====================================================

    profile = build_financial_profile(
        request
    )

    # =====================================================
    # 2. INTERNAL PROFILE → EXISTING USER MODEL
    # =====================================================

    user = profile_to_user(
        profile
    )

    # =====================================================
    # 3. RUN COMPLETE MONEYBUDDY ENGINE
    # =====================================================

    result = run_moneybuddy(
        profile,
        user
    )

    # =====================================================
    # 4. CONVERT ENGINE RESULT TO API RESPONSE SCHEMA
    # =====================================================

    api_response_dict = build_api_response(
        result
    )

    return MoneyBuddyResponse.model_validate(
        api_response_dict
    ).model_dump()