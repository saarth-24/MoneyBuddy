from dataclasses import dataclass, fields
@dataclass
class User:
    salary: float
    essential_expense: float
    debt: float
    emi: float
    interest: float
    loan_time_period: float
    emergency_fund: float
    goal: float
    goal_time_period: float
    goal_current_amount: float = 0.0

@dataclass
class Calculations:
    savingratio: float
    expenseratio:float
    debtratio:float

@dataclass
class Advice:
    metrics:Calculations
    score:float
    recommendation:list[str]
    explanation:list[str]