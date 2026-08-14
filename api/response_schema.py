from typing import List, Optional
from pydantic import BaseModel


# =========================================================
# FINANCIAL HEALTH
# =========================================================

class FinancialHealthResponse(BaseModel):
    savingratio: float
    expenseratio: float
    debtratio: float
    score: float
    recommendation: List[str]
    explanation: List[str]


# =========================================================
# GOAL
# =========================================================

class GoalResponse(BaseModel):
    target_amount: float
    current_amount: float
    remaining_amount: float
    months_remaining: int
    required_monthly_saving: float
    status: str


# =========================================================
# DEBT
# =========================================================

class DebtResponse(BaseModel):
    total_debt: float
    total_emi: float
    highest_interest_debt: str
    highest_interest_rate: float
    lowest_interest_debt: str
    lowest_interest_rate: float
    weighted_average_interest: float
    estimated_monthly_interest: float
    debt_to_income_ratio: float
    number_of_debts: int
    priority_order: List[str]


# =========================================================
# PORTFOLIO
# =========================================================

class HoldingResponse(BaseModel):
    name: str
    asset_type: str
    current_value: float
    invested_amount: float
    gain: float
    gain_percent: float
    portfolio_weight: float


class PortfolioResponse(BaseModel):
    total_value: float
    total_invested: float
    total_gain: float
    total_gain_percent: float
    number_of_investments: int
    concentration_percent: float
    largest_holding: str
    portfolio_risk: str
    diversification_status: str
    holdings: List[HoldingResponse]


# =========================================================
# INVESTMENT DECISION
# =========================================================

class InvestmentDecisionResponse(BaseModel):
    action: str
    recommended_amount: float
    reason: str
    confidence: float


# =========================================================
# RISK PROFILE
# =========================================================

class RiskProfileResponse(BaseModel):
    risk_capacity: str
    risk_tolerance: str
    overall_profile: str
    emergency_months: float
    debt_burden: float
    savings_ratio: float
    explanation: str


# =========================================================
# GOAL PRIORITY
# =========================================================

class GoalPriorityResponse(BaseModel):
    name: str
    priority_score: float
    urgency: str
    recommended_focus: str
    reason: str


# =========================================================
# PORTFOLIO RECOMMENDATION
# =========================================================

class PortfolioRecommendationResponse(BaseModel):
    action: str
    priority: str
    reason: str
    concentration: float
    risk: str
    diversification: str


# =========================================================
# SCENARIO
# =========================================================

class ScenarioResponse(BaseModel):
    scenario_name: str
    monthly_income: float
    monthly_expenses: float
    monthly_surplus: float
    debt_payment: float
    remaining_debt: float
    emergency_allocation: float
    emergency_months: float
    investment_capacity: float
    goal_monthly_requirement: float
    goal_shortfall: float
    goal_status: str
    surplus_change: float
    explanation: str


class RankedScenarioResponse(BaseModel):
    rank: int
    score: float
    scenario: ScenarioResponse


# =========================================================
# ACTION PLAN
# =========================================================

class ActionResponse(BaseModel):
    priority: int
    category: str
    action: str
    recommended_amount: float
    allocated_amount: float
    reason: str
    confidence: float


class ActionPlanResponse(BaseModel):
    summary: str
    monthly_income: float
    monthly_expenses: float
    monthly_surplus: float
    actions: List[ActionResponse]
    overall_message: str


# =========================================================
# AI CFO
# =========================================================

class CFOPriorityResponse(BaseModel):
    category: str
    action: str
    amount: float
    reason: str


class AICFOResponse(BaseModel):
    headline: str
    financial_status: str

    top_priority: CFOPriorityResponse

    secondary_priorities: List[CFOPriorityResponse]

    investment_status: str
    investment_amount: float
    investment_reason: str

    goal_status: str
    goal_shortfall: float

    why: List[str]
    next_steps: List[str]
    reassessment_triggers: List[str]

    personal_message: str


# =========================================================
# COMPLETE MONEYBUDDY RESPONSE
# =========================================================

class MoneyBuddyResponse(BaseModel):

    financial_health: FinancialHealthResponse

    goal: GoalResponse

    debt: DebtResponse

    goals_intelligence: dict

    portfolio: PortfolioResponse

    investment_decision: InvestmentDecisionResponse

    risk_profile: RiskProfileResponse

    goal_priorities: List[GoalPriorityResponse]

    portfolio_recommendation: PortfolioRecommendationResponse

    current_scenario: ScenarioResponse

    what_if_scenarios: List[RankedScenarioResponse]

    best_scenario: Optional[ScenarioResponse]

    action_plan: ActionPlanResponse

    ai_cfo: Optional[AICFOResponse]