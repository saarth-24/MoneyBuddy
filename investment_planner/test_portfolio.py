import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from user_profile.models import (
    Debt,
    Investment,
    FinancialGoal,
    FinancialProfile
)

from investment_planner.analyzer import (
    analyze_portfolio
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


analysis = analyze_portfolio(profile)


print("\n================================")
print("      PORTFOLIO ANALYSIS")
print("================================")

print(
    f"Total Value          : "
    f"₹{analysis.total_value:.2f}"
)

print(
    f"Total Invested       : "
    f"₹{analysis.total_invested:.2f}"
)

print(
    f"Total Gain           : "
    f"₹{analysis.total_gain:.2f}"
)

print(
    f"Gain %               : "
    f"{analysis.total_gain_percent:.2f}%"
)

print(
    f"Number of Investments: "
    f"{analysis.number_of_investments}"
)

print(
    f"Largest Holding      : "
    f"{analysis.largest_holding}"
)

print(
    f"Concentration        : "
    f"{analysis.concentration_percent:.2f}%"
)

print(
    f"Portfolio Risk       : "
    f"{analysis.portfolio_risk}"
)

print(
    f"Diversification      : "
    f"{analysis.diversification_status}"
)

print("================================")