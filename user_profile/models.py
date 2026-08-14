from dataclasses import dataclass, field
from typing import List


@dataclass
class Debt:
    name: str
    outstanding: float
    interest_rate: float
    emi: float
    remaining_months: int


@dataclass
class Investment:
    name: str
    asset_type: str
    current_value: float
    invested_amount: float = 0.0


@dataclass
class FinancialGoal:
    name: str
    target_amount: float
    current_amount: float
    target_months: int
    priority: int = 1


@dataclass
class FinancialProfile:
    monthly_income: float
    essential_expenses: float
    discretionary_expenses: float = 0.0
    emergency_fund: float = 0.0

    user_risk_capacity: str = "UNKNOWN"

    debts: List[Debt] = field(default_factory=list)

    investments: List[Investment] = field(default_factory=list)

    goals: List[FinancialGoal] = field(default_factory=list)

    @property
    def monthly_expenses(self) -> float:
        return (
            self.essential_expenses
            + self.discretionary_expenses
        )

    @property
    def monthly_emi(self) -> float:
        return sum(
            debt.emi
            for debt in self.debts
        )

    @property
    def total_debt(self) -> float:
        return sum(
            debt.outstanding
            for debt in self.debts
        )

    @property
    def total_investment_value(self) -> float:
        return sum(
            investment.current_value
            for investment in self.investments
        )