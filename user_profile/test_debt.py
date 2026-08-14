from user_profile.models import (
    Debt,
    Investment,
    FinancialGoal,
    FinancialProfile
)

from user_profile.debt_analyzer import (
    analyze_debts
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


analysis = analyze_debts(profile)


print("\n================================")
print("       DEBT ANALYSIS")
print("================================")

print(
    f"Total Debt : "
    f"₹{analysis.total_debt:.2f}"
)

print(
    f"Total EMI : "
    f"₹{analysis.total_emi:.2f}"
)

print(
    f"Highest Interest Debt : "
    f"{analysis.highest_interest_debt}"
)

print(
    f"Highest Interest Rate : "
    f"{analysis.highest_interest_rate:.2f}%"
)

print(
    f"Lowest Interest Debt : "
    f"{analysis.lowest_interest_debt}"
)

print(
    f"Lowest Interest Rate : "
    f"{analysis.lowest_interest_rate:.2f}%"
)

print(
    f"Weighted Average Interest : "
    f"{analysis.weighted_average_interest:.2f}%"
)

print(
    f"Estimated Monthly Interest : "
    f"₹{analysis.estimated_monthly_interest:.2f}"
)

print(
    f"Debt To Income Ratio : "
    f"{analysis.debt_to_income_ratio:.2f}%"
)

print(
    f"Number Of Debts : "
    f"{analysis.number_of_debts}"
)

print("\nDebt Priority:")

for index, debt in enumerate(
    analysis.priority_order,
    start=1
):

    print(
        f"{index}. {debt}"
    )

print("================================")