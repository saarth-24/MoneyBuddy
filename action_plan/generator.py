from ai_cfo.test_final_edge_cases import user
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from action_plan.models import ActionPlan, ActionItem

from financial_health.models import User
from decision_engine.models import FinancialDecision


def generate_action_plan(
    user: User,
    decisions: list[FinancialDecision],
    salary_plan,
    goal_analysis,
    investment_decision
) -> ActionPlan:

    # =====================================================
    # 1. BASIC FINANCIAL NUMBERS
    # =====================================================

    monthly_income = float(user.salary)

    # MoneyBuddy defines monthly cash obligations as:
    # essential expenses + mandatory EMI.
    monthly_expenses = float(user.essential_expense)

    monthly_surplus = (
        monthly_income
        - monthly_expenses
        - float(user.emi)
    )

    monthly_surplus = max(
        monthly_surplus,
        0.0
    )

    monthly_surplus = max(
        monthly_surplus,
        0.0
    )

    # =====================================================
    # 2. CONVERT DECISIONS INTO ACTION ITEMS
    # =====================================================

    actions = []

    for decision in decisions:

        actions.append(
            ActionItem(
                priority=decision.priority,
                category=decision.category,
                action=decision.action,
                recommended_amount=(
                    decision.recommended_amount
                ),
                allocated_amount=(
                    decision.allocated_amount
                ),
                reason=decision.reason,
                confidence=decision.confidence
            )
        )

    # =====================================================
    # 3. GENERATE SUMMARY
    # =====================================================

    if monthly_surplus > 0:

        summary = (
            f"You have ₹{monthly_surplus:.2f} "
            f"of estimated monthly surplus after "
            f"essential expenses and EMI."
        )

    else:

        summary = (
            "Your current income is largely consumed "
            "by essential expenses and debt obligations."
        )

    # =====================================================
    # 4. GENERATE OVERALL MESSAGE
    # =====================================================

    if decisions:

        highest_priority = decisions[0]

        message_parts = []

        # -------------------------------------------------
        # Opening situation
        # -------------------------------------------------

        message_parts.append(
            f"You currently have ₹{monthly_surplus:.2f} "
            f"of estimated monthly surplus."
        )

        # -------------------------------------------------
        # Highest priority
        # -------------------------------------------------

        message_parts.append(
            f"MoneyBuddy recommends first focusing on "
            f"{highest_priority.action.lower()}."
        )

        # -------------------------------------------------
        # Debt explanation
        # -------------------------------------------------

        if user.debt > 0 and user.interest > 12:

            message_parts.append(
                f"Your {user.interest:.0f}% debt creates a "
                f"higher financial priority than taking "
                f"additional investment risk."
            )

        # -------------------------------------------------
        # Emergency fund explanation
        # -------------------------------------------------


        # Monthly financial obligations include
        # essential expenses plus mandatory EMI.
        monthly_obligations = (
            float(user.essential_expense)
            + float(user.emi)
        )

        if monthly_obligations > 0:

            emergency_months = (
                user.emergency_fund
                / monthly_obligations
            )

            if emergency_months < 3:

                message_parts.append(
                    f"Your emergency fund currently covers "
                    f"only {emergency_months:.1f} months of "
                    f"essential obligations."
                )

        # -------------------------------------------------
        # Goal conflict
        # -------------------------------------------------

        if (
            goal_analysis
            and hasattr(goal_analysis, "status")
            and goal_analysis.status != "ON_TRACK"
        ):

            goal_allocation = 0.0

            if (
                salary_plan
                and hasattr(
                    salary_plan,
                    "goal_savings"
                )
            ):
                goal_allocation = (
                    salary_plan.goal_savings
                )

            goal_shortfall = (
                goal_analysis.required_monthly_saving
                - goal_allocation
            )

            if goal_shortfall > 0:

                message_parts.append(
                    f"Your goal requires approximately "
                    f"₹{goal_analysis.required_monthly_saving:.2f} "
                    f"per month, but your current surplus "
                    f"cannot fully fund it after higher-priority "
                    f"financial obligations."
                )

        # -------------------------------------------------
        # Investment conflict
        # -------------------------------------------------

        if (
            investment_decision
            and hasattr(
                investment_decision,
                "recommended_amount"
            )
            and investment_decision.recommended_amount == 0
        ):

            message_parts.append(
                "Although market conditions may currently "
                "be favorable, MoneyBuddy recommends delaying "
                "aggressive investment until your higher-priority "
                "financial risks improve."
            )

        # -------------------------------------------------
        # Final recommendation
        # -------------------------------------------------

        message_parts.append(
            "This allocation should be reassessed as your "
            "emergency buffer, debt position, and goal funding "
            "improve."
        )

        overall_message = " ".join(
            message_parts
        )

    else:

        overall_message = (
            "Your current financial position does not "
            "require an urgent corrective action based "
            "on the available information."
        )

    # =====================================================
    # 5. RETURN ACTION PLAN
    # =====================================================

    return ActionPlan(

        summary=summary,

        monthly_income=round(
            monthly_income,
            2
        ),

        monthly_expenses=round(
            monthly_expenses,
            2
        ),

        monthly_surplus=round(
            monthly_surplus,
            2
        ),

        actions=actions,

        overall_message=overall_message
    )