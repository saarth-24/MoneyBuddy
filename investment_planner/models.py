from dataclasses import dataclass
from typing import List


@dataclass
class HoldingAnalysis:

    name: str
    asset_type: str

    current_value: float
    invested_amount: float

    gain: float
    gain_percent: float

    portfolio_weight: float


@dataclass
class InvestmentAnalysis:

    total_value: float
    total_invested: float

    total_gain: float
    total_gain_percent: float

    number_of_investments: int

    concentration_percent: float

    largest_holding: str

    portfolio_risk: str
    diversification_status: str

    holdings: List[HoldingAnalysis]