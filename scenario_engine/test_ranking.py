from scenario_engine.engine import (
    run_scenario,
    rank_scenarios
)


current_income = 50000
current_expenses = 35000
current_emi = 13000
current_debt = 250000
emergency_fund = 20000
goal_required_monthly = 6666.67


scenarios = []


# =========================================
# 1. SALARY INCREASE
# =========================================

scenarios.append(
    run_scenario(
        scenario_name="Salary Increase",

        current_income=current_income,
        current_expenses=current_expenses,
        current_emi=current_emi,
        current_debt=current_debt,
        emergency_fund=emergency_fund,
        goal_required_monthly=goal_required_monthly,

        income_change=10000
    )
)


# =========================================
# 2. EXPENSE REDUCTION
# =========================================

scenarios.append(
    run_scenario(
        scenario_name="Expense Reduction",

        current_income=current_income,
        current_expenses=current_expenses,
        current_emi=current_emi,
        current_debt=current_debt,
        emergency_fund=emergency_fund,
        goal_required_monthly=goal_required_monthly,

        expense_change=-5000
    )
)


# =========================================
# 3. EXTRA DEBT PAYMENT
# =========================================

scenarios.append(
    run_scenario(
        scenario_name="Extra Debt Payment",

        current_income=current_income,
        current_expenses=current_expenses,
        current_emi=current_emi,
        current_debt=current_debt,
        emergency_fund=emergency_fund,
        goal_required_monthly=goal_required_monthly,

        extra_debt_payment=3000
    )
)


# =========================================
# 4. ADDITIONAL INVESTMENT
# =========================================

scenarios.append(
    run_scenario(
        scenario_name="Additional Investment",

        current_income=current_income,
        current_expenses=current_expenses,
        current_emi=current_emi,
        current_debt=current_debt,
        emergency_fund=emergency_fund,
        goal_required_monthly=goal_required_monthly,

        additional_investment=2000
    )
)


# =========================================
# RANK
# =========================================

ranked = rank_scenarios(
    scenarios
)


print("\n========================================")
print("       MONEYBUDDY SCENARIO RANKING")
print("========================================")


for item in ranked:

    scenario = item["scenario"]

    print(
        f"\nRank : {item['rank']}"
    )

    print(
        f"Score : {item['score']:.2f}"
    )

    print(
        f"Scenario : {scenario.scenario_name}"
    )

    print(
        f"Monthly Surplus : "
        f"₹{scenario.monthly_surplus:.2f}"
    )

    print(
        f"Investment Capacity : "
        f"₹{scenario.investment_capacity:.2f}"
    )

    print(
        f"Goal Status : "
        f"{scenario.goal_status}"
    )

    print(
        f"Surplus Change : "
        f"₹{scenario.surplus_change:.2f}"
    )

print("\n========================================")