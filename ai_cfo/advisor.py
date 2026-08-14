from ai_cfo.client import AICFOClient

from ai_cfo.models import (
    CFOResponse,
    CFOPriority
)

from ai_cfo.prompt import (
    build_system_prompt,
    build_user_prompt
)


# =========================================================
# DETERMINISTIC FALLBACK
# =========================================================

def _generate_fallback_cfo_response(
    decisions,
    investment_decision,
    goal_analysis,
    salary_plan
):
    """
    Deterministic fallback used when Gemini is unavailable
    or returns an invalid/unsafe response.

    IMPORTANT:
    This function does NOT make financial decisions.

    It only uses decisions already produced by the
    MoneyBuddy Python financial engine.
    """

    if not decisions:
        raise ValueError(
            "MoneyBuddy decision engine returned no decisions."
        )

    # -----------------------------------------------------
    # TOP PRIORITY
    # -----------------------------------------------------

    highest_decision = decisions[0]

    top_priority = CFOPriority(
        category=highest_decision.category,

        action=highest_decision.action,

        amount=float(
            highest_decision.allocated_amount
        ),

        reason=highest_decision.reason
    )

    # -----------------------------------------------------
    # SECONDARY PRIORITIES
    # -----------------------------------------------------

    secondary_priorities = []

    for decision in decisions[1:]:

        secondary_priorities.append(
            CFOPriority(
                category=decision.category,

                action=decision.action,

                amount=float(
                    decision.allocated_amount
                ),

                reason=decision.reason
            )
        )

    # -----------------------------------------------------
    # GOAL SHORTFALL
    # -----------------------------------------------------

    goal_shortfall = max(
        float(
            goal_analysis.required_monthly_saving
        )
        - float(
            salary_plan.goal_savings
        ),
        0.0
    )

    # -----------------------------------------------------
    # WHY
    # -----------------------------------------------------

    why = [
        decision.reason
        for decision in decisions[:3]
    ]

    if not why:
        why = [
            "Financial priorities were determined by "
            "the MoneyBuddy decision engine."
        ]

    # -----------------------------------------------------
    # NEXT STEPS
    # -----------------------------------------------------

    next_steps = [
        (
            f"Follow the highest-priority action: "
            f"{highest_decision.action}."
        ),

        (
            f"Use the allocated amount of "
            f"₹{highest_decision.allocated_amount:.2f} "
            f"determined by the MoneyBuddy engine."
        ),

        (
            "Reassess the plan after a significant "
            "change in income, expenses, debt, "
            "emergency savings, or financial goals."
        )
    ]

    # -----------------------------------------------------
    # REASSESSMENT TRIGGERS
    # -----------------------------------------------------

    reassessment_triggers = [
        "Significant change in monthly income.",

        "Significant change in essential expenses.",

        "Major reduction or repayment of high-interest debt.",

        "Emergency fund reaches the target level."
    ]

    # -----------------------------------------------------
    # FINAL FALLBACK RESPONSE
    # -----------------------------------------------------

    return CFOResponse(

        headline=(
            "MoneyBuddy Financial Action Plan"
        ),

        financial_status=(
            "AI personalization is temporarily "
            "unavailable. This recommendation is "
            "based directly on the verified "
            "MoneyBuddy financial decision engine."
        ),

        top_priority=top_priority,

        secondary_priorities=secondary_priorities,

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

        why=why,

        next_steps=next_steps,

        reassessment_triggers=(
            reassessment_triggers
        ),

        personal_message=(
            "MoneyBuddy is currently using its "
            "verified financial decision engine "
            "to provide your financial action plan."
        )
    )


# =========================================================
# MAIN AI CFO FUNCTION
# =========================================================

def generate_cfo_advice(
    user,
    health_advice,
    salary_plan,
    goal_analysis,
    market_analysis,
    investment_decision,
    decisions,
    risk_profile,
    goal_priorities,
    portfolio_recommendation,
    scenario,
    what_if_scenarios=None
):

    # =====================================================
    # 1. NORMALIZE WHAT-IF SCENARIOS
    # =====================================================

    if what_if_scenarios is None:
        what_if_scenarios = []

    # =====================================================
    # 2. VALIDATE MONEYBUDDY DECISION ENGINE
    # =====================================================

    if not decisions:

        raise ValueError(
            "MoneyBuddy decision engine returned no decisions."
        )

    # Python engine is ALWAYS the source of truth.

    highest_decision = decisions[0]

    # =====================================================
    # 3. BUILD PROMPTS
    # =====================================================

    system_prompt = build_system_prompt()

    user_prompt = build_user_prompt(
        user=user,
        health_advice=health_advice,
        salary_plan=salary_plan,
        goal_analysis=goal_analysis,
        market_analysis=market_analysis,
        investment_decision=investment_decision,
        decisions=decisions,
        risk_profile=risk_profile,
        goal_priorities=goal_priorities,
        portfolio_recommendation=portfolio_recommendation,
        scenario=scenario,
        what_if_scenarios=what_if_scenarios
    )

    # =====================================================
    # 4. CALL GEMINI
    # =====================================================

    try:

        client = AICFOClient()

        data = client.generate_advice(
            system_prompt=system_prompt,
            user_prompt=user_prompt
        )

    except Exception as error:

        print()
        print(
            "[MoneyBuddy] AI CFO unavailable."
        )

        print(
            "[MoneyBuddy] Using deterministic "
            "financial-engine fallback."
        )

        print(
            f"[MoneyBuddy] Reason: {error}"
        )

        return _generate_fallback_cfo_response(
            decisions=decisions,
            investment_decision=investment_decision,
            goal_analysis=goal_analysis,
            salary_plan=salary_plan
        )

    # =====================================================
    # 5. VALIDATE GEMINI RESPONSE
    # =====================================================

    try:

        if not isinstance(data, dict):

            raise ValueError(
                "Gemini returned an invalid CFO response. "
                "Expected a JSON object."
            )

        # =================================================
        # 6. TOP PRIORITY
        # =================================================

        top_priority_data = data.get(
            "top_priority",
            {}
        )

        if not isinstance(
            top_priority_data,
            dict
        ):
            top_priority_data = {}

        engine_top_category = (
            highest_decision.category
        )

        engine_top_action = (
            highest_decision.action
        )

        engine_top_amount = float(
            highest_decision.allocated_amount
        )

        engine_top_reason = (
            highest_decision.reason
        )

        top_priority = CFOPriority(

            category=top_priority_data.get(
                "category",
                engine_top_category
            ),

            action=top_priority_data.get(
                "action",
                engine_top_action
            ),

            amount=float(
                top_priority_data.get(
                    "amount",
                    engine_top_amount
                )
            ),

            reason=top_priority_data.get(
                "reason",
                engine_top_reason
            )
        )

        # =================================================
        # 7. VALIDATE TOP PRIORITY
        # =================================================

        if top_priority.category != engine_top_category:

            raise ValueError(
                "AI CFO changed the highest-priority "
                "category. "
                f"MoneyBuddy engine says "
                f"{engine_top_category}, "
                f"but AI returned "
                f"{top_priority.category}."
            )

        if top_priority.action != engine_top_action:

            raise ValueError(
                "AI CFO changed the highest-priority "
                "action. "
                f"MoneyBuddy engine says "
                f"'{engine_top_action}', "
                f"but AI returned "
                f"'{top_priority.action}'."
            )

        if abs(
            top_priority.amount
            - engine_top_amount
        ) > 0.01:

            raise ValueError(
                "AI CFO changed the highest-priority "
                "allocation. "
                f"MoneyBuddy engine says "
                f"₹{engine_top_amount:.2f}, "
                f"but AI returned "
                f"₹{top_priority.amount:.2f}."
            )

        # =================================================
        # 8. SECONDARY PRIORITIES
        # =================================================

        secondary_data = data.get(
            "secondary_priorities",
            []
        )

        if not isinstance(
            secondary_data,
            list
        ):
            secondary_data = []

        engine_secondary_decisions = decisions[1:]

        if len(secondary_data) != len(
            engine_secondary_decisions
        ):

            raise ValueError(
                "AI CFO returned an incorrect number "
                "of secondary priorities. "
                f"MoneyBuddy engine has "
                f"{len(engine_secondary_decisions)} "
                f"secondary decisions, but AI returned "
                f"{len(secondary_data)}."
            )

        secondary_priorities = []

        for index, engine_decision in enumerate(
            engine_secondary_decisions
        ):

            item = secondary_data[index]

            if not isinstance(
                item,
                dict
            ):

                raise ValueError(
                    "AI CFO returned an invalid "
                    "secondary priority."
                )

            engine_category = (
                engine_decision.category
            )

            engine_action = (
                engine_decision.action
            )

            engine_amount = float(
                engine_decision.allocated_amount
            )

            engine_reason = (
                engine_decision.reason
            )

            ai_category = item.get(
                "category",
                engine_category
            )

            ai_action = item.get(
                "action",
                engine_action
            )

            ai_amount = float(
                item.get(
                    "amount",
                    engine_amount
                )
            )

            ai_reason = item.get(
                "reason",
                engine_reason
            )

            # ---------------------------------------------
            # VALIDATE CATEGORY
            # ---------------------------------------------

            if ai_category != engine_category:

                raise ValueError(
                    "AI CFO changed a secondary priority "
                    "category. "
                    f"MoneyBuddy engine says "
                    f"{engine_category}, "
                    f"but AI returned "
                    f"{ai_category}."
                )

            # ---------------------------------------------
            # VALIDATE ACTION
            # ---------------------------------------------

            if ai_action != engine_action:

                raise ValueError(
                    "AI CFO changed a secondary priority "
                    "action. "
                    f"MoneyBuddy engine says "
                    f"'{engine_action}', "
                    f"but AI returned "
                    f"'{ai_action}'."
                )

            # ---------------------------------------------
            # VALIDATE ALLOCATION
            # ---------------------------------------------

            if abs(
                ai_amount
                - engine_amount
            ) > 0.01:

                raise ValueError(
                    "AI CFO changed a secondary priority "
                    "allocation. "
                    f"Category: {engine_category}. "
                    f"MoneyBuddy engine says "
                    f"₹{engine_amount:.2f}, "
                    f"but AI returned "
                    f"₹{ai_amount:.2f}."
                )

            secondary_priorities.append(
                CFOPriority(
                    category=ai_category,
                    action=ai_action,
                    amount=ai_amount,
                    reason=ai_reason
                )
            )

        # =================================================
        # 9. INVESTMENT INFORMATION
        # =================================================

        engine_investment_amount = float(
            investment_decision.recommended_amount
        )

        investment_amount = float(
            data.get(
                "investment_amount",
                engine_investment_amount
            )
        )

        investment_status = data.get(
            "investment_status",
            getattr(
                investment_decision,
                "action",
                "HOLD"
            )
        )

        investment_reason = data.get(
            "investment_reason",
            getattr(
                investment_decision,
                "reason",
                ""
            )
        )

        # =================================================
        # 10. VALIDATE INVESTMENT
        # =================================================

        if abs(
            investment_amount
            - engine_investment_amount
        ) > 0.01:

            raise ValueError(
                "AI CFO changed the investment allocation. "
                f"MoneyBuddy engine says "
                f"₹{engine_investment_amount:.2f}, "
                f"but AI returned "
                f"₹{investment_amount:.2f}."
            )

        # =================================================
        # 11. GOAL INFORMATION
        # =================================================

        engine_goal_status = (
            goal_analysis.status
        )

        goal_status = data.get(
            "goal_status",
            engine_goal_status
        )

        # Python calculates actual goal shortfall.

        engine_goal_shortfall = max(
            float(
                goal_analysis.required_monthly_saving
            )
            - float(
                salary_plan.goal_savings
            ),
            0.0
        )

        goal_shortfall = float(
            data.get(
                "goal_shortfall",
                engine_goal_shortfall
            )
        )

        # =================================================
        # 12. VALIDATE GOAL STATUS
        # =================================================

        if goal_status != engine_goal_status:

            raise ValueError(
                "AI CFO changed the goal status. "
                f"MoneyBuddy engine says "
                f"{engine_goal_status}, "
                f"but AI returned "
                f"{goal_status}."
            )

        # =================================================
        # 13. VALIDATE GOAL SHORTFALL
        # =================================================

        if abs(
            goal_shortfall
            - engine_goal_shortfall
        ) > 0.01:

            raise ValueError(
                "AI CFO changed the goal shortfall. "
                f"MoneyBuddy engine says "
                f"₹{engine_goal_shortfall:.2f}, "
                f"but AI returned "
                f"₹{goal_shortfall:.2f}."
            )

        # =================================================
        # 14. READ EXPLANATIONS
        # =================================================

        why = data.get(
            "why",
            []
        )

        next_steps = data.get(
            "next_steps",
            []
        )

        reassessment_triggers = data.get(
            "reassessment_triggers",
            []
        )

        personal_message = data.get(
            "personal_message",
            ""
        )

        # =================================================
        # 15. CLEAN LIST VALUES
        # =================================================

        if not isinstance(
            why,
            list
        ):
            why = [str(why)]

        if not isinstance(
            next_steps,
            list
        ):
            next_steps = [str(next_steps)]

        if not isinstance(
            reassessment_triggers,
            list
        ):
            reassessment_triggers = [
                str(reassessment_triggers)
            ]

        why = [
            str(item)
            for item in why
        ]

        next_steps = [
            str(item)
            for item in next_steps
        ]

        reassessment_triggers = [
            str(item)
            for item in reassessment_triggers
        ]

        # =================================================
        # 16. VALIDATE WHAT-IF RANKING INTEGRITY
        # =================================================

        # Ranking is calculated by Python.
        # Gemini only explains it.

        if what_if_scenarios:

            def _has_field(
                obj_or_dict,
                field_name
            ):

                if isinstance(
                    obj_or_dict,
                    dict
                ):

                    return field_name in obj_or_dict

                return hasattr(
                    obj_or_dict,
                    field_name
                )

            for index, item in enumerate(
                what_if_scenarios,
                start=1
            ):

                scenario_obj = (
                    item.get(
                        "scenario",
                        item
                    )
                    if isinstance(
                        item,
                        dict
                    )
                    else item
                )

                if not _has_field(
                    scenario_obj,
                    "scenario_name"
                ):

                    raise ValueError(
                        "Invalid What-If scenario supplied "
                        "to AI CFO."
                    )

                if not _has_field(
                    scenario_obj,
                    "monthly_surplus"
                ):

                    raise ValueError(
                        "What-If scenario is missing "
                        "monthly_surplus."
                    )

                if not _has_field(
                    scenario_obj,
                    "goal_status"
                ):

                    raise ValueError(
                        "What-If scenario is missing "
                        "goal_status."
                    )

        # =================================================
        # 17. CREATE FINAL CFO RESPONSE
        # =================================================

        return CFOResponse(

            headline=data.get(
                "headline",
                "MoneyBuddy AI CFO Analysis"
            ),

            financial_status=data.get(
                "financial_status",
                "Financial status evaluated."
            ),

            top_priority=top_priority,

            secondary_priorities=(
                secondary_priorities
            ),

            investment_status=(
                investment_status
            ),

            investment_amount=(
                investment_amount
            ),

            investment_reason=(
                investment_reason
            ),

            goal_status=(
                goal_status
            ),

            goal_shortfall=(
                goal_shortfall
            ),

            why=why,

            next_steps=(
                next_steps
            ),

            reassessment_triggers=(
                reassessment_triggers
            ),

            personal_message=(
                personal_message
            )
        )

    # =====================================================
    # 18. AI RESPONSE FAILED VALIDATION
    # =====================================================

    except Exception as error:

        print()
        print(
            "[MoneyBuddy] AI CFO response failed "
            "validation."
        )

        print(
            "[MoneyBuddy] Using deterministic "
            "financial-engine fallback."
        )

        print(
            f"[MoneyBuddy] Reason: {error}"
        )

        return _generate_fallback_cfo_response(
            decisions=decisions,
            investment_decision=investment_decision,
            goal_analysis=goal_analysis,
            salary_plan=salary_plan
        )