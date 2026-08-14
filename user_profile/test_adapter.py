import sys

if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from user_profile import (
    Debt,
    Investment,
    FinancialGoal,
    FinancialProfile,
    validate_profile,
    profile_to_user
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
        ),

        Debt(
            name="Credit Card",
            outstanding=50000,
            interest_rate=24,
            emi=3000,
            remaining_months=24
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

user = profile_to_user(profile)


print("\n==============================")
print("     ADAPTER TEST")
print("==============================")

print(
    f"Salary              : ₹{user.salary:.2f}"
)

print(
    f"Essential Expense   : ₹{user.essential_expense:.2f}"
)

print(
    f"Total Expense       : ₹{profile.monthly_expenses:.2f}"
)

print(
    f"Total Debt          : ₹{user.debt:.2f}"
)

print(
    f"Total EMI           : ₹{user.emi:.2f}"
)

print(
    f"Selected Interest   : {user.interest:.2f}%"
)

print(
    f"Goal                : ₹{user.goal:.2f}"
)

print(
    f"Goal Period         : {user.goal_time_period:.2f} years"
)

print("==============================")
print("ADAPTER WORKING")
print("==============================")