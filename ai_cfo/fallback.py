from ai_cfo.models import CFOResponse, CFOPriority


def generate_fallback_cfo_response(
    decisions,
    investment_decision,
    goal_analysis,
    salary_plan
):
    if not decisions:
        raise ValueError(
            "Cannot generate fallback CFO response "
            "without decision-engine decisions."
        )

    top = decisions[0]

    secondary = []

    for decision in decisions[1:]:
        secondary.append(
            CFOPriority(
                category=decision.category,
                action=decision.action,
                amount=float(
                    decision.allocated_amount
                ),
                reason=decision.reason
            )
        )

    goal_shortfall = max(
        goal_analysis.required_monthly_saving
        - salary_plan.goal_savings,
        0
    )

    return CFOResponse(
        headline=(
            "MoneyBuddy Financial Action Plan"
        ),

        financial_status=(
            "AI-generated personalization is "
            "temporarily unavailable. "
            "The following recommendations are "
            "based directly on the MoneyBuddy "
            "financial decision engine."
        ),

        top_priority=CFOPriority(
            category=top.category,
            action=top.action,
            amount=float(
                top.allocated_amount
            ),
            reason=top.reason
        ),

        secondary_priorities=secondary,

        investment_status=(
            investment_decision.action
        ),

        investment_amount=float(
            investment_decision.recommended_amount
        ),

        investment_reason=(
            investment_decision.reason
        ),

        goal_status=(
            goal_analysis.status
        ),

        goal_shortfall=float(
            goal_shortfall
        ),

        why=[
            decision.reason
            for decision in decisions[:3]
        ],

        next_steps=[
            (
                f"Follow the highest-priority action: "
                f"{top.action}."
            ),
            (
                f"Follow the allocated amount of "
                f"₹{top.allocated_amount:.2f} "
                f"determined by the MoneyBuddy engine."
            ),
            (
                "Reassess the financial plan after "
                "a significant change in income, "
                "expenses, debt or emergency savings."
            )
        ],

        reassessment_triggers=[
            "Significant change in monthly income.",
            "Significant change in essential expenses.",
            "Major reduction in high-interest debt.",
            "Emergency fund reaches the target level."
        ],

        personal_message=(
            "MoneyBuddy is currently using its "
            "verified financial decision engine "
            "to provide your action plan."
        )
    )