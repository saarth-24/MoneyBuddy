from dataclasses import dataclass
from typing import List


@dataclass
class GoalPriority:

    name: str
    priority_score: float
    urgency: str
    recommended_focus: str
    reason: str


def prioritize_goals(
    goals
) -> List[GoalPriority]:

    results = []

    for goal in goals:

        remaining = max(
            goal.target_amount
            - goal.current_amount,
            0
        )

        if goal.target_amount > 0:

            progress = (
                goal.current_amount
                / goal.target_amount
            ) * 100

        else:

            progress = 100

        months = max(
            goal.target_months,
            1
        )

        required_monthly = (
            remaining / months
        )

        # -------------------------------------
        # URGENCY
        # -------------------------------------

        if months <= 12:
            urgency = "HIGH"
            urgency_score = 40

        elif months <= 36:
            urgency = "MODERATE"
            urgency_score = 25

        else:
            urgency = "LOW"
            urgency_score = 10

        # -------------------------------------
        # FUNDING GAP
        # -------------------------------------

        if progress < 25:

            gap_score = 30

        elif progress < 50:

            gap_score = 20

        else:

            gap_score = 10

        # -------------------------------------
        # PRIORITY
        # -------------------------------------

        score = (
            urgency_score
            + gap_score
            + goal.priority
        )

        if score >= 60:

            focus = "HIGH"

        elif score >= 40:

            focus = "MEDIUM"

        else:

            focus = "LOW"

        reason = (
            f"{goal.name} has {progress:.1f}% "
            f"completion and requires approximately "
            f"₹{required_monthly:.2f} per month."
        )

        results.append(

            GoalPriority(

                name=goal.name,

                priority_score=round(
                    score,
                    2
                ),

                urgency=urgency,

                recommended_focus=focus,

                reason=reason
            )
        )

    results.sort(
        key=lambda x:
        x.priority_score,
        reverse=True
    )

    return results