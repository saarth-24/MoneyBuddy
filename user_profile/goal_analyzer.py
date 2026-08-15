from dataclasses import dataclass
from typing import List

from user_profile.models import FinancialProfile


@dataclass
class GoalAnalysisResult:

    name: str

    target_amount: float
    current_amount: float
    remaining_amount: float

    months_remaining: int

    required_monthly_saving: float

    priority: int

    status: str


@dataclass
class GoalsAnalysis:

    total_goals: int
    total_target: float
    total_current: float

    highest_priority_goal: str

    goals: List[GoalAnalysisResult]


def analyze_goals(
    profile: FinancialProfile,
    monthly_available_for_goal: float = None
) -> GoalsAnalysis:

    goals = profile.goals

    if not goals:

        return GoalsAnalysis(
            total_goals=0,
            total_target=0.0,
            total_current=0.0,
            highest_priority_goal="NONE",
            goals=[]
        )

    # -----------------------------------------
    # AVAILABLE MONTHLY SURPLUS
    # -----------------------------------------

    if monthly_available_for_goal is None:

        total_emi = sum(
            debt.emi
            for debt in profile.debts
        )

        monthly_available_for_goal = (
            profile.monthly_income
            - profile.essential_expenses
            - profile.discretionary_expenses
            - total_emi
        )

        monthly_available_for_goal = max(
            monthly_available_for_goal,
            0.0
        )

    results = []

    for goal in goals:

        remaining = max(
            goal.target_amount
            - goal.current_amount,
            0.0
        )

        months = max(
            goal.target_months,
            1
        )

        required_monthly = (
            remaining / months
        )

        # -----------------------------------------
        # GOAL STATUS
        # -----------------------------------------

        if remaining <= 0:

            status = "COMPLETED"

        elif required_monthly <= monthly_available_for_goal:

            status = "ON_TRACK"

        else:

            status = "AT_RISK"

        results.append(

            GoalAnalysisResult(

                name=goal.name,

                target_amount=round(
                    goal.target_amount,
                    2
                ),

                current_amount=round(
                    goal.current_amount,
                    2
                ),

                remaining_amount=round(
                    remaining,
                    2
                ),

                months_remaining=months,

                required_monthly_saving=round(
                    required_monthly,
                    2
                ),

                priority=goal.priority,

                status=status
            )
        )

    results.sort(
        key=lambda goal: goal.priority
    )

    return GoalsAnalysis(

        total_goals=len(goals),

        total_target=round(
            sum(
                goal.target_amount
                for goal in goals
            ),
            2
        ),

        total_current=round(
            sum(
                goal.current_amount
                for goal in goals
            ),
            2
        ),

        highest_priority_goal=(
            results[0].name
        ),

        goals=results
    )