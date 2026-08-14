import sys

if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from user_profile import (
    Debt,
    Investment,
    FinancialGoal,
    FinancialProfile,
    validate_profile
)


profile = FinancialProfile(

    monthly_income=50000,

    essential_expenses=35000,

    discretionary_expenses=1000,

    emergency_fund=20000,

    debts=[
        Debt(
            name="Personal Loan",
            outstanding=200000,
            interest_rate=15,
            emi=10000,
            remaining_months=36
        )
    ],

    investments=[
        Investment(
            name="INFY",
            asset_type="STOCK",
            current_value=25000,
            invested_amount=22000
        )
    ],

    goals=[
        FinancialGoal(
            name="House Goal",
            target_amount=500000,
            current_amount=100000,
            target_months=60,
            priority=1
        )
    ]
)


validate_profile(profile)


print("\n==============================")
print("   USER PROFILE TEST")
print("==============================")

print(
    f"Monthly Income       : ₹{profile.monthly_income:.2f}"
)

print(
    f"Monthly Expenses     : ₹{profile.monthly_expenses:.2f}"
)

print(
    f"Monthly EMI          : ₹{profile.monthly_emi:.2f}"
)

print(
    f"Total Debt           : ₹{profile.total_debt:.2f}"
)

print(
    f"Emergency Fund       : ₹{profile.emergency_fund:.2f}"
)

print(
    f"Investment Value     : ₹{profile.total_investment_value:.2f}"
)

print(
    f"Number of Debts      : {len(profile.debts)}"
)

print(
    f"Number of Investments: {len(profile.investments)}"
)

print(
    f"Number of Goals      : {len(profile.goals)}"
)

print("==============================")
print("PROFILE VALID")
print("==============================")