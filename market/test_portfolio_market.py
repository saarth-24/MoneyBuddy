from user_profile.models import (
    Debt,
    Investment,
    FinancialGoal,
    FinancialProfile
)

from market.client import TwelveDataClient

from market.portfolio_market import (
    analyze_profile_markets
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


client = TwelveDataClient()

results = analyze_profile_markets(
    profile,
    client
)


print("\n================================")
print("     PROFILE MARKET ANALYSIS")
print("================================")

for symbol, analysis in results.items():

    print(
        f"\nAsset : {symbol}"
    )

    if isinstance(analysis, dict):

        print(
            f"Error : {analysis['error']}"
        )

        continue

    print(
        f"Price : ₹"
        f"{analysis.current_price:.2f}"
    )

    print(
        f"Return : "
        f"{analysis.return_percent:.2f}%"
    )

    print(
        f"Volatility : "
        f"{analysis.volatility_percent:.2f}%"
    )

    print(
        f"Trend : "
        f"{analysis.trend}"
    )

    print(
        f"Risk : "
        f"{analysis.risk_level}"
    )

    print(
        f"Signal : "
        f"{analysis.momentum}"
    )

print("================================")