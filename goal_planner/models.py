from dataclasses import dataclass


@dataclass
class GoalAnalysis:
    target_amount: float
    current_amount: float
    remaining_amount: float
    months_remaining: int
    required_monthly_saving: float
    status: str