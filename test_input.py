import json

from api.schemas import FinancialProfileRequest
from api.adapter import build_financial_profile
from user_profile.adapter import profile_to_user
from financial_health.metrics import calculate
from api.service import analyze_financial_profile


# =========================================================
# 1. TEST INPUT
# =========================================================

request = FinancialProfileRequest(
    name="Test User",
    age=20,
    city="Delhi",
    employment_type="SALARIED",
    family_dependents=0,

    monthly_income=50000,
    total_expense=30000,

    rent=0,
    subscriptions_bills=0,
    household=0,
    lifestyle=0,
    family_dependencies_expense=0,

    primary_operating_bank="HDFC",
    liquid_savings_bank="SBI",
    active_credit_card=True,

    loan_emi=15000,
    loan_category="PERSONAL",
    lending_bank="HDFC",
    interest_rate=14,
    loan_time_period=10,
    remaining_principal=500000,

    emergency_fund=30000,

    risk_taking_capacity="MEDIUM",

    goal="Buy a house",
    goal_time_period=5,
    goal_amount=500000,
    goal_current_amount=50000,

    portfolio=[]
)


# =========================================================
# 2. EXPECTED VALUES
# =========================================================

EXPECTED_INCOME = 50000
EXPECTED_EXPENSE = 30000
EXPECTED_EMI = 15000
EXPECTED_DEBT = 500000
EXPECTED_SURPLUS = 5000
EXPECTED_EMERGENCY = 30000
EXPECTED_GOAL_REMAINING = 450000
EXPECTED_GOAL_MONTHLY = 7500


# =========================================================
# 3. INPUT VALIDATION
# =========================================================

print("\n========================================")
print("       MONEYBUDDY FULL PIPELINE TEST")
print("========================================")

print("\n[1] INPUT")

print("Income       :", request.monthly_income)
print("Total expense:", request.total_expense)
print("EMI          :", request.loan_emi)
print("Debt         :", request.remaining_principal)
print("Emergency    :", request.emergency_fund)
print("Goal         :", request.goal_amount)
print("Goal current :", request.goal_current_amount)
print("Goal period  :", request.goal_time_period)


# =========================================================
# 4. PROFILE CONVERSION
# =========================================================

profile = build_financial_profile(request)

print("\n[2] FINANCIAL PROFILE")

print("Income              :", profile.monthly_income)
print("Total expenses      :", profile.monthly_expenses)
print("Essential expenses  :", profile.essential_expenses)
print("Discretionary       :", profile.discretionary_expenses)
print("Total debt          :", profile.total_debt)
print("Monthly EMI         :", profile.monthly_emi)
print("Emergency fund      :", profile.emergency_fund)


# =========================================================
# 5. USER MODEL CONVERSION
# =========================================================

user = profile_to_user(profile)

print("\n[3] USER MODEL")

print("Salary              :", user.salary)
print("Expense             :", user.essential_expense)
print("EMI                 :", user.emi)
print("Debt                :", user.debt)
print("Emergency fund      :", user.emergency_fund)


# =========================================================
# 6. FINANCIAL HEALTH CALCULATION
# =========================================================

metrics = calculate(user)

print("\n[4] FINANCIAL HEALTH")

print("Saving ratio        :", metrics.savingratio)
print("Expense ratio       :", metrics.expenseratio)
print("Debt ratio          :", metrics.debtratio)


# =========================================================
# 7. FULL MONEYBUDDY ENGINE
# =========================================================

print("\n[5] RUNNING COMPLETE MONEYBUDDY ENGINE...")

response = analyze_financial_profile(
    request
)


# =========================================================
# 8. FINAL OUTPUT
# =========================================================

print("\n[6] FINAL MONEYBUDDY OUTPUT")

action_plan = response.get("action_plan") or {}

print("Income              :", action_plan.get("monthly_income"))
print("Expenses            :", action_plan.get("monthly_expenses"))
print("Surplus             :", action_plan.get("monthly_surplus"))


goal = response.get("goal")

print("\nGoal output:")
print(json.dumps(
    goal,
    indent=2,
    ensure_ascii=False
))


debt = response.get("debt")

print("\nDebt output:")
print(json.dumps(
    debt,
    indent=2,
    ensure_ascii=False
))


# =========================================================
# 9. AUTOMATIC CHECKS
# =========================================================

print("\n========================================")
print("           AUTOMATIC CHECKS")
print("========================================")


def check(name, actual, expected):

    if actual == expected:
        print(f"PASS  {name}: {actual}")

    else:
        print(
            f"FAIL  {name}: "
            f"expected {expected}, "
            f"got {actual}"
        )


check(
    "Income",
    profile.monthly_income,
    EXPECTED_INCOME
)

check(
    "Total expenses",
    profile.monthly_expenses,
    EXPECTED_EXPENSE
)

check(
    "User expense",
    user.essential_expense,
    EXPECTED_EXPENSE
)

check(
    "EMI",
    user.emi,
    EXPECTED_EMI
)

check(
    "Debt",
    user.debt,
    EXPECTED_DEBT
)

check(
    "Expected surplus",
    EXPECTED_INCOME
    - EXPECTED_EXPENSE
    - EXPECTED_EMI,
    EXPECTED_SURPLUS
)

check(
    "Final action-plan surplus",
    action_plan.get("monthly_surplus"),
    EXPECTED_SURPLUS
)


# =========================================================
# 10. GOAL CHECK
# =========================================================

if goal:

    goal_data = goal

    remaining = (
        goal_data.get("remaining_amount")
    )

    required_monthly = (
        goal_data.get("required_monthly_saving")
    )

    check(
        "Goal remaining",
        remaining,
        EXPECTED_GOAL_REMAINING
    )

    check(
        "Goal monthly requirement",
        required_monthly,
        EXPECTED_GOAL_MONTHLY
    )


# =========================================================
# 11. COMPLETE RESPONSE
# =========================================================

print("\n========================================")
print("        COMPLETE API RESPONSE")
print("========================================")

print(
    json.dumps(
        response,
        indent=2,
        ensure_ascii=False
    )
)

print("\n========================================")
print("             TEST COMPLETE")
print("========================================")


print("\n========== TEST INPUT ==========")

print("Monthly income       :", request.monthly_income)
print("Total expense        :", request.total_expense)

print("Rent                 :", request.rent)
print("Subscriptions/bills  :", request.subscriptions_bills)
print("Household            :", request.household)
print("Lifestyle            :", request.lifestyle)
print("Family dependencies  :", request.family_dependencies_expense)

print("Loan EMI             :", request.loan_emi)
print("Loan category        :", request.loan_category)
print("Interest rate        :", request.interest_rate)
print("Loan period          :", request.loan_time_period)
print("Remaining principal  :", request.remaining_principal)

print("Emergency fund       :", request.emergency_fund)

print("Goal                 :", request.goal)
print("Goal amount          :", request.goal_amount)
print("Current goal amount  :", request.goal_current_amount)
print("Goal period          :", request.goal_time_period)

print("================================\n")



profile = build_financial_profile(request)
user = profile_to_user(profile)
metrics = calculate(user)

print("\n========== INTERNAL DATA ==========")

print("Profile income      :", profile.monthly_income)
print("Profile expenses    :", profile.monthly_expenses)
print("Essential expenses  :", profile.essential_expenses)
print("Discretionary       :", profile.discretionary_expenses)

print("User income         :", user.salary)
print("User expense       :", user.essential_expense)
print("User EMI            :", user.emi)
print("User debt           :", user.debt)

print("\n========== CALCULATIONS ==========")

print("Saving ratio        :", metrics.savingratio)
print("Expense ratio       :", metrics.expenseratio)
print("Debt ratio          :", metrics.debtratio)

print("\nExpected surplus    :",
      request.monthly_income
      - request.total_expense
      - request.loan_emi)

print("===================================")


from api.service import analyze_financial_profile

print("\n========== FULL MONEYBUDDY TEST ==========")

response = analyze_financial_profile(request)

print("\nMonthly income:")
print(response["action_plan"]["monthly_income"])

print("\nMonthly expenses:")
print(response["action_plan"]["monthly_expenses"])

print("\nMonthly surplus:")
print(response["action_plan"]["monthly_surplus"])

print("\nEMI:")
print(response["debt"])

print("\nGoal:")
print(response["goal"])

print("\n==========================================")