import json

from api.schemas import FinancialProfileRequest
from api.service import analyze_financial_profile
from api.response import build_api_response


def main():

    request = FinancialProfileRequest(

        name="Test User",

        age=28,

        city="Delhi",

        employment_type="SALARIED",

        family_dependents=2,

        monthly_income=50000,

        total_expense=36000,

        rent=10000,

        subscriptions_bills=3000,

        household=10000,

        lifestyle=3000,

        family_dependencies_expense=10000,

        primary_operating_bank="HDFC",

        liquid_savings_bank="SBI",

        active_credit_card=True,

        loan_emi=13000,

        loan_category="PERSONAL_LOAN",

        lending_bank="ICICI",

        interest_rate=24,

        loan_time_period=3,

        remaining_principal=250000,

        emergency_fund=20000,

        risk_taking_capacity="MODERATE",

        goal="HOUSE",

        goal_time_period=5,

        goal_amount=500000,

        goal_current_amount=100000,

        portfolio=[
            {
                "symbol": "INFY",
                "current_value": 25000,
                "invested_amount": 22000
            }
        ]
    )

    print()
    print("========================================")
    print("       MONEYBUDDY API RESPONSE TEST")
    print("========================================")

    response = analyze_financial_profile(
        request
    )

    print(
        json.dumps(
            response,
            indent=2,
            ensure_ascii=False
        )
    )

    print()
    print("========================================")
    print("       API RESPONSE TEST COMPLETE")
    print("========================================")


if __name__ == "__main__":
    main()