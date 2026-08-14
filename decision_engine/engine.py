from decision_engine.models import FinancialDecision

from financial_health.models import User, Advice
from salary_planner.models import SalaryPlan
from goal_planner.models import GoalAnalysis


def make_decisions(
    user: User,
    health_advice: Advice,
    salary_plan: SalaryPlan,
    goal_analysis: GoalAnalysis,
    investment_decision=None
):

    decisions = []

    # =====================================================
    # 1. EMERGENCY FUND
    # =====================================================

    monthly_obligations = (
        user.essential_expense +
        user.emi
    )

    if user.emergency_fund < (monthly_obligations * 3):

        emergency_shortfall = (
            (monthly_obligations * 3) - user.emergency_fund
        )

        decisions.append(
            FinancialDecision(

                priority=1,

                category="EMERGENCY_FUND",

                action="Build emergency fund",

                recommended_amount=(
                    salary_plan.emergency_fund
                ),

                allocated_amount=(
                    salary_plan.emergency_fund
                ),

                reason=(
                    f"Your emergency fund currently covers "
                    f"only {round(user.emergency_fund / monthly_obligations if monthly_obligations > 0 else 0, 1)} "
                    f"months of essential financial obligations. "
                    f"MoneyBuddy recommends strengthening your "
                    f"emergency buffer before increasing "
                    f"investment risk."
                ),

                confidence=90.0
            )
        )


    # =====================================================
    # 2. DEBT
    # =====================================================

    if user.debt > 0 and user.interest > 12:

        decisions.append(
            FinancialDecision(

                priority=2,

                category="DEBT",

                action="Prioritize high-interest debt repayment",

                recommended_amount=(
                    salary_plan.debt_payment
                ),

                allocated_amount=(
                    salary_plan.debt_payment
                ),

                reason=(
                    f"Your outstanding debt carries an interest rate "
                    f"of {user.interest}%. "
                    f"Reducing expensive debt can provide "
                    f"a more predictable financial benefit "
                    f"than taking additional investment risk."
                ),

                confidence=95.0
            )
        )


    # =====================================================
    # 3. GOAL
    # =====================================================

    if goal_analysis.status != "ON_TRACK":

        shortfall = (
            goal_analysis.required_monthly_saving
            - salary_plan.goal_savings
        )

        if shortfall < 0:
            shortfall = 0

        decisions.append(
            FinancialDecision(

                priority=3,

                category="GOAL",

                action=(
                    "Increase goal contribution when "
                    "higher-priority obligations are under control"
                ),

                recommended_amount=(
                    goal_analysis.required_monthly_saving
                ),

                allocated_amount=(
                    salary_plan.goal_savings
                ),

                reason=(
                    f"Your goal requires approximately "
                    f"₹{goal_analysis.required_monthly_saving:.2f} "
                    f"per month. Your current plan allocates "
                    f"₹{salary_plan.goal_savings:.2f}. "
                    f"This creates a monthly goal funding "
                    f"shortfall of approximately "
                    f"₹{shortfall:.2f}."
                ),

                confidence=85.0
            )
        )


    # =====================================================
    # 4. INVESTMENT
    # =====================================================

    if investment_decision and investment_decision.recommended_amount > 0:

        decisions.append(
            FinancialDecision(

                priority=4,

                category="INVESTMENT",

                action=(
                    investment_decision.action
                ),

                recommended_amount=(
                    investment_decision.recommended_amount
                ),

                allocated_amount=(
                    salary_plan.investments
                ),

                reason=(
                    investment_decision.reason
                ),

                confidence=(
                    investment_decision.confidence
                )
            )
        )


    # =====================================================
    # 5. SORT BY PRIORITY
    # =====================================================

    decisions.sort(
        key=lambda decision: decision.priority
    )


    return decisions









if __name__ == "__main__":

    from financial_health.models import (
        User,
        Calculations,
        Advice
    )

    from salary_planner.allocator import (
        create_salary_plan
    )

    from goal_planner.calculator import (
        calculate_goal
    )


    # -----------------------------
    # SAMPLE USER
    # -----------------------------

    user = User(
        salary=50000,
        essential_expense=35000,
        debt=200000,
        emi=10000,
        interest=15,
        loan_time_period=3,
        emergency_fund=20000,
        goal=500000,
        goal_time_period=5
    )


    # -----------------------------
    # HEALTH DATA
    # -----------------------------

    metrics = Calculations(
        savingratio=10,
        expenseratio=90,
        debtratio=40
    )


    advice = Advice(
        metrics=metrics,
        score=45,
        recommendation=[
            "PAY_OFF_DEBT",
            "INCREASE_SAVINGS"
        ],
        explanation=[
            "High debt detected."
        ]
    )


    # -----------------------------
    # SALARY PLAN
    # -----------------------------

    salary_plan = create_salary_plan(
        user,
        advice
    )


    # -----------------------------
    # GOAL ANALYSIS
    # -----------------------------

    goal_analysis = calculate_goal(
        target_amount=500000,
        current_amount=100000,
        time_period_years=5,
        monthly_available_for_goal=5000
    )


    # -----------------------------
    # DECISION ENGINE
    # -----------------------------

    decisions = make_decisions(
        user,
        advice,
        salary_plan,
        goal_analysis
    )


    # -----------------------------
    # DISPLAY
    # -----------------------------

    print("\n================================")
    print("       MONEYBUDDY DECISIONS")
    print("================================")

    for decision in decisions:

        print(
            f"\nPriority : {decision.priority}"
        )

        print(
            f"Category : {decision.category}"
        )

        print(
            f"Action   : {decision.action}"
        )

        print(
            f"Recommended : ₹{decision.recommended_amount:.2f}"
        )

        print(
            f"Allocated   : ₹{decision.allocated_amount:.2f}"
        )

        print(
            f"Reason   : {decision.reason}"
        )

        print(
            f"Confidence : {decision.confidence}%"
        )

    print("\n================================")