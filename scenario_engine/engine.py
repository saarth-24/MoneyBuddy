from dataclasses import dataclass


@dataclass
class ScenarioResult:

    scenario_name: str

    monthly_income: float
    monthly_expenses: float
    monthly_surplus: float

    debt_payment: float
    remaining_debt: float

    emergency_allocation: float
    emergency_months: float

    investment_capacity: float

    goal_monthly_requirement: float
    goal_shortfall: float
    goal_status: str

    surplus_change: float

    explanation: str


def run_scenario(
    scenario_name: str,

    current_income: float,
    current_expenses: float,
    current_emi: float,
    current_debt: float,
    emergency_fund: float,

    goal_required_monthly: float,

    emergency_allocation: float = 0.0,
    debt_allocation: float = 0.0,
    goal_allocation: float = 0.0,
    investment_allocation: float = 0.0,

    income_change: float = 0.0,
    expense_change: float = 0.0,
    extra_debt_payment: float = 0.0,
    additional_investment: float = 0.0
) -> ScenarioResult:

    # =====================================================
    # 1. NEW INCOME / EXPENSES / DEBT PAYMENT
    # =====================================================

    new_income = (
        current_income
        + income_change
    )

    new_expenses = max(
        current_expenses
        + expense_change,
        0
    )

    new_debt_payment = (
        current_emi
        + extra_debt_payment
    )


    # =====================================================
    # 2. CURRENT SURPLUS
    # =====================================================

    current_surplus = (
        current_income
        - current_expenses
        - current_emi
    )

    current_surplus = max(
        current_surplus,
        0
    )


    # =====================================================
    # 3. NEW SURPLUS
    # =====================================================

    new_surplus = (
        new_income
        - new_expenses
        - new_debt_payment
    )

    new_surplus = max(
        new_surplus,
        0
    )


    surplus_change = (
        new_surplus
        - current_surplus
    )


    # =====================================================
    # 4. EMERGENCY ALLOCATION
    # =====================================================

    emergency_allocation = max(
        emergency_allocation,
        0
    )

    emergency_allocation = min(
        emergency_allocation,
        new_surplus
    )


    # =====================================================
    # 5. INVESTMENT CAPACITY
    # =====================================================

    investment_capacity = max(
        new_surplus
        - emergency_allocation
        - additional_investment,
        0
    )


    # =====================================================
    # 6. REMAINING AMOUNT AVAILABLE FOR GOAL
    # =====================================================

    remaining_after_priorities = max(
        new_surplus
        - emergency_allocation
        - extra_debt_payment
        - additional_investment,
        0
    )


    # IMPORTANT:
    #
    # goal_allocation represents the amount that is
    # actually directed toward the goal.
    #
    # We do NOT automatically treat the entire surplus
    # as goal funding.

    actual_goal_allocation = min(
        max(goal_allocation, 0),
        remaining_after_priorities
    )


    # =====================================================
    # 7. GOAL SHORTFALL
    # =====================================================

    goal_shortfall = max(
        goal_required_monthly
        - actual_goal_allocation,
        0
    )


    # =====================================================
    # 8. GOAL STATUS
    # =====================================================

    if goal_required_monthly <= 0:

        goal_status = "NO_GOAL"

    elif goal_shortfall <= 0:

        goal_status = "ON_TRACK"

    else:

        goal_status = "AT_RISK"


    # =====================================================
    # 9. REMAINING DEBT
    # =====================================================

    remaining_debt = max(
        current_debt
        - extra_debt_payment,
        0
    )


    # =====================================================
    # 10. EMERGENCY COVERAGE
    # =====================================================

    monthly_obligations = (
        new_expenses
        + new_debt_payment
    )

    if monthly_obligations > 0:

        emergency_months = (
            emergency_fund
            + emergency_allocation
        ) / monthly_obligations

    else:

        emergency_months = 0.0


    # =====================================================
    # 11. EXPLANATION
    # =====================================================

    if surplus_change > 0:

        change_text = (
            f"₹{surplus_change:.2f} higher"
        )

    elif surplus_change < 0:

        change_text = (
            f"₹{abs(surplus_change):.2f} lower"
        )

    else:

        change_text = "unchanged"


    explanation = (
        f"{scenario_name} changes your estimated "
        f"monthly surplus to ₹{new_surplus:.2f}, "
        f"which is {change_text} than your current "
        f"surplus. "
        f"₹{actual_goal_allocation:.2f} is allocated "
        f"toward the goal under this scenario. "
        f"The goal requires "
        f"₹{goal_required_monthly:.2f} per month, "
        f"leaving a monthly shortfall of "
        f"₹{goal_shortfall:.2f}. "
        f"Your goal would be "
        f"{goal_status.lower()}."
    )


    # =====================================================
    # 12. RETURN RESULT
    # =====================================================

    return ScenarioResult(

        scenario_name=scenario_name,

        monthly_income=round(
            new_income,
            2
        ),

        monthly_expenses=round(
            new_expenses,
            2
        ),

        monthly_surplus=round(
            new_surplus,
            2
        ),

        debt_payment=round(
            new_debt_payment,
            2
        ),

        remaining_debt=round(
            remaining_debt,
            2
        ),

        emergency_allocation=round(
            emergency_allocation,
            2
        ),

        emergency_months=round(
            emergency_months,
            2
        ),

        investment_capacity=round(
            investment_capacity,
            2
        ),

        goal_monthly_requirement=round(
            goal_required_monthly,
            2
        ),

        goal_shortfall=round(
            goal_shortfall,
            2
        ),

        goal_status=goal_status,

        surplus_change=round(
            surplus_change,
            2
        ),

        explanation=explanation
    )


# =========================================================
# SCENARIO RANKING
# =========================================================

def rank_scenarios(
    scenarios
):

    ranked = []

    for scenario in scenarios:

        score = 0.0

        # Goal status
        if scenario.goal_status == "ON_TRACK":
            score += 50

        elif scenario.goal_status == "AT_RISK":
            score -= 20


        # Surplus improvement
        score += (
            scenario.surplus_change
            / 1000
        )


        # Investment capacity
        score += min(
            scenario.investment_capacity / 1000,
            20
        )


        # Goal shortfall penalty
        score -= min(
            scenario.goal_shortfall / 1000,
            30
        )


        ranked.append({

            "scenario": scenario,

            "score": round(
                score,
                2
            )
        })


    ranked.sort(
        key=lambda item:
        item["score"],
        reverse=True
    )


    for index, item in enumerate(
        ranked,
        start=1
    ):

        item["rank"] = index


    return ranked