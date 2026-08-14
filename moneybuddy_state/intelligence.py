from types import SimpleNamespace

from risk_engine.profiler import calculate_risk_profile
from goal_engine.prioritizer import prioritize_goals
from portfolio_engine.recommender import (
    recommend_portfolio_action
)
from scenario_engine.engine import run_scenario


def build_intelligence(
    user,
    health_advice,
    goal_analysis,
    portfolio_analysis
):
    """
    Builds the higher-level intelligence layer
    used by MoneyBuddy's AI CFO.
    """

    # =====================================================
    # 1. RISK PROFILE
    # =====================================================

    risk_profile = calculate_risk_profile(
        monthly_income=user.salary,

        essential_expenses=(
            user.essential_expense
        ),

        emi=user.emi,

        emergency_fund=(
            user.emergency_fund
        ),

        savings_ratio=(
            health_advice.metrics.savingratio
        ),

        debt_ratio=(
            health_advice.metrics.debtratio
        ),

        investment_experience="UNKNOWN"
    )

    # =====================================================
    # 2. GOAL PRIORITIZATION
    # =====================================================

    goal = SimpleNamespace(
        name="Primary Goal",

        target_amount=(
            goal_analysis.target_amount
        ),

        current_amount=(
            goal_analysis.current_amount
        ),

        target_months=max(
            int(
                user.goal_time_period * 12
            ),
            1
        ),

        priority=1
    )

    goal_priorities = prioritize_goals(
        [goal]
    )

    # =====================================================
    # 3. PORTFOLIO RECOMMENDATION
    # =====================================================

    portfolio_recommendation = (
        recommend_portfolio_action(

            concentration=(
                portfolio_analysis.concentration_percent
            ),

            risk=(
                portfolio_analysis.portfolio_risk
            ),

            diversification=(
                portfolio_analysis.diversification_status
            )
        )
    )

    # =====================================================
    # 4. BASE SCENARIO
    # =====================================================

    scenario = run_scenario(

        scenario_name="Current Financial Position",

        current_income=(
            user.salary
        ),

        current_expenses=(
            user.essential_expense
        ),

        current_emi=(
            user.emi
        ),

        current_debt=(
            user.debt
        ),

        emergency_fund=(
            user.emergency_fund
        ),

        goal_required_monthly=(
            goal_analysis.required_monthly_saving
        )
    )

    return {
        "risk_profile": risk_profile,

        "goal_priorities": goal_priorities,

        "portfolio_recommendation":
            portfolio_recommendation,

        "scenario": scenario
    }