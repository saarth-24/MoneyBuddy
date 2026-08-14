from dataclasses import dataclass
from typing import Optional, Any, List


@dataclass
class MoneyBuddyState:

    user: Any

    health_advice: Any

    salary_plan: Any

    goal_analysis: Any

    debt_analysis: Any

    goals_analysis: Any

    market_analysis: Any

    portfolio_analysis: Any

    investment_decision: Any

    decisions: List[Any]

    action_plan: Any

    risk_profile: Optional[Any] = None

    scenario_analysis: Optional[Any] = None

    goal_priorities: Optional[Any] = None

    portfolio_recommendation: Optional[Any] = None

    ai_advice: Optional[Any] = None