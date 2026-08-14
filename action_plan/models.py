from dataclasses import dataclass
from typing import List


@dataclass
class ActionItem:

    priority: int
    category: str
    action: str

    recommended_amount: float
    allocated_amount: float

    reason: str
    confidence: float


@dataclass
class ActionPlan:

    summary: str

    monthly_income: float
    monthly_expenses: float
    monthly_surplus: float

    actions: List[ActionItem]

    overall_message: str