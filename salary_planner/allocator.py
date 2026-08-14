import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from salary_planner.models import SalaryPlan
from financial_health.models import User, Advice, Calculations

def create_salary_plan(user: User, health_advice: Advice):
    salary = user.salary
    actual_expense = user.essential_expense + user.emi
  
    real_surplus = salary - actual_expense

    # DEFICIT SCENARIO
    if real_surplus <= 0:
        return SalaryPlan(
            actual_expense=round(actual_expense, 2),
            emergency_fund=0.0,
            debt_payment=0.0,
            investments=0.0,
            goal_savings=0.0,
            leisure=0.0,
            remaining_balance=round(real_surplus, 2)  
        )

    # Sanity Cushion (10% of surplus reserved for Leisure)
    base_leisure = real_surplus * 0.10
    remaining_cash = real_surplus - base_leisure

    # Financial Diagnostics
    emergency_months = user.emergency_fund / actual_expense if actual_expense > 0 else 0
    needs_emergency_fund = emergency_months < 6

    debt_service_ratio = (user.emi / salary) * 100 if salary > 0 else 0
    has_high_debt_burden = debt_service_ratio > 30
    has_high_interest_debt = user.interest > 12

    is_in_firefighting_mode = has_high_interest_debt or has_high_debt_burden or needs_emergency_fund

    debt_payment = 0.0
    emergency_fund = 0.0
    goal_savings = 0.0
    investments = 0.0

    # -------------------------------------------------------------
    # STAGE 1: Emergency Fund (First Line of Defense)
    # -------------------------------------------------------------
    if needs_emergency_fund and remaining_cash > 0:
        emergency_target = actual_expense * 6
        emergency_gap = max(0, emergency_target - user.emergency_fund)
        
        # Take up to 50% of surplus to build Emergency Buffer
        emergency_fund = min(remaining_cash * 0.50, emergency_gap)
        remaining_cash -= emergency_fund

    # -------------------------------------------------------------
    # STAGE 2: High-Interest Debt (Aggressive Laser Focus)
    # -------------------------------------------------------------
    if (has_high_interest_debt or has_high_debt_burden) and remaining_cash > 0:
        # Redirect ALL remaining surplus into Debt Payment!
        debt_payment = remaining_cash
        remaining_cash = 0.0

    # -------------------------------------------------------------
    # STAGE 3 & 4: Goals & Investments (ONLY if NOT in Firefighting Mode!)
    # -------------------------------------------------------------
    if not is_in_firefighting_mode and remaining_cash > 0:
        if user.goal_time_period > 0:
            monthly_goal_req = user.goal / (user.goal_time_period * 12)
            goal_savings = min(remaining_cash * 0.50, monthly_goal_req)
            remaining_cash -= goal_savings

        if remaining_cash > 0:
            investments = remaining_cash * 0.70
            remaining_cash -= investments

    # Leftover cash rolls back into leisure/wants
    total_leisure = base_leisure + remaining_cash

    return SalaryPlan(
        actual_expense=round(actual_expense, 2),
        emergency_fund=round(emergency_fund, 2),
        debt_payment=round(debt_payment, 2),
        investments=round(investments, 2),
        goal_savings=round(goal_savings, 2),
        leisure=round(total_leisure, 2),
        remaining_balance=round(remaining_cash, 2)
    )


if __name__ == "__main__":
    # 1. Create a sample user
    sample_user = User(
        salary=50000,
        essential_expense=35000,
        debt=200000,
        emi=10000,
        interest=15,
        loan_time_period=3,
        emergency_fund=20000,
        goal=500000,
        goal_time_period=5,
        goal_current_amount=0
    )
  

    # 2. Create mock health advice (Health score = 45 due to high debt)
    sample_metrics = Calculations(savingratio=35.0, expenseratio=65.0, debtratio=40.0)
    sample_advice = Advice(
        metrics=sample_metrics,
        score=45.0,
        recommendation=["PAY_OFF_DEBT", "INCREASE_SAVINGS"],
        explanation=["High debt ratio detected."]
    )

    # 3. Run Salary Planner
    plan = create_salary_plan(sample_user, sample_advice)

    # 4. Print results
    print("DEBUG salary:", sample_user.salary)
    print("DEBUG essential expense:", sample_user.essential_expense)
    print("DEBUG EMI:", sample_user.emi)
    print("DEBUG total expense:", plan.actual_expense)

    print("\n==========================================")
    print("      MONEYBUDDY AI: SALARY PLAN          ")
    print("==========================================")
    print(f"Monthly Salary     : ${sample_user.salary}")
    print(f"Debt Payment       : ${plan.debt_payment}")
    print(f"Emergency Fund     : ${plan.emergency_fund}")
    print(f"Investments        : ${plan.investments}")
    print(f"Goal Savings       : ${plan.goal_savings}")
    print(f"Leisure / Wants    : ${plan.leisure}")
    print(f"Remaining Balance  : ${plan.remaining_balance}")
    print("==========================================\n")