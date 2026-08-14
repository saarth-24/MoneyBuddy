from dataclasses import dataclass
from typing import List


@dataclass
class PricePoint:
    date: str
    close: float


@dataclass
class MarketData:
    symbol: str
    exchange: str
    currency: str
    prices: List[PricePoint]


@dataclass
class MarketSignal:
    symbol: str
    latest_price: float
    change_7d: float
    change_30d: float
    volatility: float
    trend: str


@dataclass
class MarketAnalysis:
    symbol: str
    exchange: str
    currency: str
    current_price: float
    return_percent: float
    volatility_percent: float
    trend: str
    risk_level: str
    momentum: str