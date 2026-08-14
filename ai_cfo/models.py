from dataclasses import dataclass
from typing import List


# ============================================================
# CFO PRIORITY
# ============================================================

@dataclass
class CFOPriority:

    category: str
    action: str
    amount: float
    reason: str


# ============================================================
# CFO RESPONSE
# ============================================================

@dataclass
class CFOResponse:

    headline: str

    financial_status: str

    top_priority: CFOPriority

    secondary_priorities: List[CFOPriority]

    investment_status: str

    investment_amount: float

    investment_reason: str

    goal_status: str

    goal_shortfall: float

    why: List[str]

    next_steps: List[str]

    reassessment_triggers: List[str]

    personal_message: str


# ============================================================
# COMPATIBILITY ALIASES
# ============================================================

AITopPriority = CFOPriority

AISecondaryPriority = CFOPriority

AICFOAdvice = CFOResponse