from dataclasses import dataclass


@dataclass
class FinancialDecision:

    priority: int
    category: str
    action: str
    reason: str

    recommended_amount: float = 0.0
    allocated_amount: float = 0.0

    confidence: float = 0.0