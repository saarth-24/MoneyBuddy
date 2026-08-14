from pydantic import BaseModel, Field
from typing import List


class PortfolioHolding(BaseModel):
    symbol: str
    current_value: float = Field(ge=0)
    invested_amount: float = Field(ge=0)


class FinancialProfileRequest(BaseModel):

    # ==========================================
    # PERSONAL INFORMATION
    # ==========================================

    name: str
    age: int = Field(gt=0)
    city: str
    employment_type: str
    family_dependents: int = Field(ge=0)

    # ==========================================
    # MONTHLY INCOME / EXPENSES
    # ==========================================

    monthly_income: float = Field(ge=0)

    total_expense: float = Field(ge=0)

    rent: float = Field(default=0, ge=0)
    subscriptions_bills: float = Field(default=0, ge=0)
    household: float = Field(default=0, ge=0)
    lifestyle: float = Field(default=0, ge=0)
    family_dependencies_expense: float = Field(
        default=0,
        ge=0
    )

    # ==========================================
    # BANKING
    # ==========================================

    primary_operating_bank: str
    liquid_savings_bank: str
    active_credit_card: bool

    # ==========================================
    # LOAN / DEBT
    # ==========================================

    loan_emi: float = Field(default=0, ge=0)
    loan_category: str = "NONE"
    lending_bank: str = ""

    interest_rate: float = Field(
        default=0,
        ge=0
    )

    loan_time_period: float = Field(
        default=0,
        ge=0
    )

    remaining_principal: float = Field(
        default=0,
        ge=0
    )

    # ==========================================
    # EMERGENCY FUND
    # ==========================================

    emergency_fund: float = Field(
        default=0,
        ge=0
    )

    # ==========================================
    # RISK
    # ==========================================

    risk_taking_capacity: str

    # ==========================================
    # GOAL
    # ==========================================

    goal: str

    goal_time_period: float = Field(
        gt=0
    )

    goal_amount: float = Field(
        gt=0
    )

    goal_current_amount: float = Field(
        default=0,
        ge=0
    )

    # ==========================================
    # INVESTMENT PORTFOLIO
    # ==========================================

    portfolio: List[PortfolioHolding] = []