from scenario_engine.engine import run_scenario


# ==================================================
# BASE DATA
# ==================================================

income = 50000
expenses = 35000
emi = 13000

debt = 250000

emergency_fund = 20000

goal_required = 6666.67


# ==================================================
# 1. SALARY INCREASE
# ==================================================

salary_scenario = run_scenario(

    scenario_name="Salary Increase",

    current_income=income,
    current_expenses=expenses,
    current_emi=emi,

    current_debt=debt,

    emergency_fund=emergency_fund,

    goal_required_monthly=goal_required,

    income_change=10000
)


# ==================================================
# 2. EXPENSE REDUCTION
# ==================================================

expense_scenario = run_scenario(

    scenario_name="Expense Reduction",

    current_income=income,
    current_expenses=expenses,
    current_emi=emi,

    current_debt=debt,

    emergency_fund=emergency_fund,

    goal_required_monthly=goal_required,

    expense_change=-5000
)


# ==================================================
# 3. EXTRA DEBT PAYMENT
# ==================================================

debt_scenario = run_scenario(

    scenario_name="Extra Debt Payment",

    current_income=income,
    current_expenses=expenses,
    current_emi=emi,

    current_debt=debt,

    emergency_fund=emergency_fund,

    goal_required_monthly=goal_required,

    extra_debt_payment=3000
)


# ==================================================
# 4. ADDITIONAL INVESTMENT
# ==================================================

investment_scenario = run_scenario(

    scenario_name="Additional Investment",

    current_income=income,
    current_expenses=expenses,
    current_emi=emi,

    current_debt=debt,

    emergency_fund=emergency_fund,

    goal_required_monthly=goal_required,

    additional_investment=2000
)


# ==================================================
# DISPLAY
# ==================================================

scenarios = [
    salary_scenario,
    expense_scenario,
    debt_scenario,
    investment_scenario
]


print("\n========================================")
print("       MONEYBUDDY WHAT-IF ANALYSIS")
print("========================================")


for scenario in scenarios:

    print("\n----------------------------------------")

    print(
        f"Scenario : {scenario.scenario_name}"
    )

    print(
        f"Monthly Income : "
        f"₹{scenario.monthly_income:.2f}"
    )

    print(
        f"Monthly Expenses : "
        f"₹{scenario.monthly_expenses:.2f}"
    )

    print(
        f"Monthly Surplus : "
        f"₹{scenario.monthly_surplus:.2f}"
    )

    print(
        f"Debt Payment : "
        f"₹{scenario.debt_payment:.2f}"
    )

    print(
        f"Remaining Debt : "
        f"₹{scenario.remaining_debt:.2f}"
    )

    print(
        f"Emergency Coverage : "
        f"{scenario.emergency_months:.2f} months"
    )

    print(
        f"Investment Capacity : "
        f"₹{scenario.investment_capacity:.2f}"
    )

    print(
        f"Goal Requirement : "
        f"₹{scenario.goal_monthly_requirement:.2f}"
    )

    print(
        f"Goal Shortfall : "
        f"₹{scenario.goal_shortfall:.2f}"
    )

    print(
        f"Goal Status : "
        f"{scenario.goal_status}"
    )

    print(
        f"Explanation : "
        f"{scenario.explanation}"
    )


print("\n========================================")