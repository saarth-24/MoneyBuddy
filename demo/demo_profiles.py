"""
MoneyBuddy AI - Final Demo Profiles

Run from the project root:

    python -m demo.demo_profiles

This demonstrates how MoneyBuddy reacts to three different
financial situations.
"""

from user_profile import (
    Debt,
    Investment,
    FinancialGoal,
    FinancialProfile,
)

from main import run_moneybuddy


# =========================================================
# PROFILE 1
# FINANCIALLY WEAK
# =========================================================

def weak_profile():

    return FinancialProfile(
        monthly_income=40000.0,

        essential_expenses=30000.0,

        emergency_fund=10000.0,

        debts=[
            Debt(
                name="Credit Card",
                outstanding=200000.0,
                interest_rate=24.0,
                emi=8000.0,
                remaining_months=24,
            )
        ],

        investments=[
            Investment(
                name="INFY",
                asset_type="STOCK",
                current_value=11750.0,
                invested_amount=10000.0,
            )
        ],

        goals=[
            FinancialGoal(
                name="House Goal",
                target_amount=500000.0,
                current_amount=50000.0,
                target_months=60,
                priority=1,
            )
        ],
    )


# =========================================================
# PROFILE 2
# FINANCIALLY HEALTHY
# =========================================================

def healthy_profile():

    return FinancialProfile(
        monthly_income=120000.0,

        essential_expenses=45000.0,

        emergency_fund=300000.0,

        debts=[
            Debt(
                name="Home Loan",
                outstanding=500000.0,
                interest_rate=8.0,
                emi=10000.0,
                remaining_months=50,
            )
        ],

        investments=[
            Investment(
                name="INFY",
                asset_type="STOCK",
                current_value=23500.0,
                invested_amount=18000.0,
            ),
            Investment(
                name="TCS",
                asset_type="STOCK",
                current_value=35000.0,
                invested_amount=30000.0,
            ),
        ],

        goals=[
            FinancialGoal(
                name="Wealth Goal",
                target_amount=1000000.0,
                current_amount=400000.0,
                target_months=60,
                priority=1,
            )
        ],
    )


# =========================================================
# PROFILE 3
# GOAL-FOCUSED
# =========================================================

def goal_focused_profile():

    return FinancialProfile(
        monthly_income=90000.0,

        essential_expenses=40000.0,

        emergency_fund=150000.0,

        debts=[
            Debt(
                name="Home Loan",
                outstanding=800000.0,
                interest_rate=8.5,
                emi=15000.0,
                remaining_months=60,
            )
        ],

        investments=[
            Investment(
                name="INFY",
                asset_type="STOCK",
                current_value=11750.0,
                invested_amount=10000.0,
            ),
            Investment(
                name="TCS",
                asset_type="STOCK",
                current_value=17500.0,
                invested_amount=15000.0,
            ),
        ],

        goals=[
            FinancialGoal(
                name="House Down Payment",
                target_amount=1000000.0,
                current_amount=700000.0,
                target_months=12,
                priority=1,
            )
        ],
    )


# =========================================================
# DISPLAY RESULT
# =========================================================

def print_demo_result(profile_name, result):

    print()
    print("=" * 60)
    print(profile_name.upper())
    print("=" * 60)

    if not isinstance(result, dict):
        print("❌ Unexpected result format")
        return

    health = result.get("health_advice")
    investment = result.get("investment_decision")
    risk = result.get("risk_profile")
    goal = result.get("goal_analysis")
    best = result.get("best_scenario")
    decisions = result.get("decisions", [])

    print()
    print("FINANCIAL HEALTH")
    print("-" * 40)

    if health:
        print(f"Health Score       : {health.score:.1f}/100")
        print(
            f"Savings Ratio      : "
            f"{health.metrics.savingratio:.1f}%"
        )
        print(
            f"Expense Ratio      : "
            f"{health.metrics.expenseratio:.1f}%"
        )
        print(
            f"Debt Ratio         : "
            f"{health.metrics.debtratio:.1f}%"
        )

    print()
    print("RISK PROFILE")
    print("-" * 40)

    if risk:
        print(
            f"Risk Capacity      : "
            f"{risk.risk_capacity}"
        )
        print(
            f"Risk Tolerance     : "
            f"{risk.risk_tolerance}"
        )
        print(
            f"Overall Profile    : "
            f"{risk.overall_profile}"
        )
        print(
            f"Emergency Coverage : "
            f"{risk.emergency_months:.2f} months"
        )

    print()
    print("INVESTMENT DECISION")
    print("-" * 40)

    if investment:
        print(
            f"Action             : "
            f"{investment.action}"
        )
        print(
            f"Recommended Amount : "
            f"₹{investment.recommended_amount:.2f}"
        )

    print()
    print("GOAL")
    print("-" * 40)

    if goal:
        print(
            f"Target             : "
            f"₹{goal.target_amount:.2f}"
        )
        print(
            f"Current            : "
            f"₹{goal.current_amount:.2f}"
        )
        print(
            f"Required Monthly   : "
            f"₹{goal.required_monthly_saving:.2f}"
        )
        print(
            f"Status              : "
            f"{goal.status}"
        )

    print()
    print("TOP DECISION")
    print("-" * 40)

    if decisions:

        top = decisions[0]

        print(
            f"Category           : "
            f"{top.category}"
        )
        print(
            f"Action             : "
            f"{top.action}"
        )
        print(
            f"Recommended        : "
            f"₹{top.recommended_amount:.2f}"
        )

    print()
    print("BEST WHAT-IF SCENARIO")
    print("-" * 40)

    if best:

        print(
            f"Scenario            : "
            f"{best.scenario_name}"
        )
        print(
            f"Monthly Surplus     : "
            f"₹{best.monthly_surplus:.2f}"
        )
        print(
            f"Investment Capacity : "
            f"₹{best.investment_capacity:.2f}"
        )
        print(
            f"Goal Status         : "
            f"{best.goal_status}"
        )
        print(
            f"Surplus Change      : "
            f"₹{best.surplus_change:.2f}"
        )

    print()
    print("-" * 60)


# =========================================================
# MAIN
# =========================================================

def main():

    profiles = [

        (
            "USER A - FINANCIALLY WEAK",
            weak_profile()
        ),

        (
            "USER B - FINANCIALLY HEALTHY",
            healthy_profile()
        ),

        (
            "USER C - GOAL FOCUSED",
            goal_focused_profile()
        ),
    ]

    print()
    print("=" * 60)
    print("             MONEYBUDDY AI")
    print("          FINAL PROFILE DEMO")
    print("=" * 60)

    for name, profile in profiles:

        try:

            result = run_moneybuddy(
                profile
            )

            print_demo_result(
                name,
                result
            )

        except Exception as error:

            print()
            print("=" * 60)
            print(name)
            print("=" * 60)

            print()
            print("❌ PROFILE FAILED")
            print()
            print(
                f"Error: {error}"
            )

    print()
    print("=" * 60)
    print("             DEMO COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()