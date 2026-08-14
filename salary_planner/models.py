# salary_planner/models.py
from dataclasses import dataclass

@dataclass
class SalaryPlan:
    """
    Represents the allocation destination of a user's monthly income.
    All values are absolute financial amounts (e.g., in USD or INR).
    """
    emergency_fund: float
    debt_payment: float
    investments: float
    goal_savings: float
    leisure: float
    remaining_balance: float
    actual_expense: float 