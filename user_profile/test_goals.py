from user_profile.models import (
    Debt,
    Investment,
    FinancialGoal,
    FinancialProfile
)

from user_profile.goal_analyzer import (
    analyze_goals
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
        ),

        FinancialGoal(
            name="Car Goal",
            target_amount=300000,
            current_amount=50000,
            target_months=36,
            priority=2
        )

    ]
)


analysis = analyze_goals(profile)


print("\n================================")
print("       GOALS ANALYSIS")
print("================================")

print(
    f"Total Goals : "
    f"{analysis.total_goals}"
)

print(
    f"Total Target : "
    f"₹{analysis.total_target:.2f}"
)

print(
    f"Total Current : "
    f"₹{analysis.total_current:.2f}"
)

print(
    f"Highest Priority : "
    f"{analysis.highest_priority_goal}"
)

print("\nGOALS")

for goal in analysis.goals:

    print(
        f"\nName : {goal.name}"
    )

    print(
        f"Priority : {goal.priority}"
    )

    print(
        f"Target : ₹{goal.target_amount:.2f}"
    )

    print(
        f"Current : ₹{goal.current_amount:.2f}"
    )

    print(
        f"Remaining : ₹{goal.remaining_amount:.2f}"
    )

    print(
        f"Required Monthly : "
        f"₹{goal.required_monthly_saving:.2f}"
    )

    print(
        f"Status : {goal.status}"
    )

print("================================")