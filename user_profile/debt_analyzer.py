from dataclasses import dataclass
from typing import List

from user_profile.models import FinancialProfile, Debt


@dataclass
class DebtAnalysis:

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


def analyze_debts(
    profile: FinancialProfile
) -> DebtAnalysis:

    debts = profile.debts

    if not debts:

        return DebtAnalysis(
            total_debt=0.0,
            total_emi=0.0,
            highest_interest_debt="NONE",
            highest_interest_rate=0.0,
            lowest_interest_debt="NONE",
            lowest_interest_rate=0.0,
            weighted_average_interest=0.0,
            estimated_monthly_interest=0.0,
            debt_to_income_ratio=0.0,
            number_of_debts=0,
            priority_order=[]
        )

    total_debt = sum(
        debt.outstanding
        for debt in debts
    )

    total_emi = sum(
        debt.emi
        for debt in debts
    )

    highest_interest = max(
        debts,
        key=lambda debt: debt.interest_rate
    )

    lowest_interest = min(
        debts,
        key=lambda debt: debt.interest_rate
    )

    weighted_interest = (
        sum(
            debt.outstanding * debt.interest_rate
            for debt in debts
        )
        / total_debt
        if total_debt > 0
        else 0.0
    )

    estimated_monthly_interest = sum(
        debt.outstanding
        * debt.interest_rate
        / 100
        / 12
        for debt in debts
    )

    if profile.monthly_income > 0:

        debt_to_income_ratio = (
            total_emi
            / profile.monthly_income
        ) * 100

    else:

        debt_to_income_ratio = 0.0

    priority_debts = sorted(
        debts,
        key=lambda debt: debt.interest_rate,
        reverse=True
    )

    priority_order = [
        debt.name
        for debt in priority_debts
    ]

    return DebtAnalysis(

        total_debt=round(
            total_debt,
            2
        ),

        total_emi=round(
            total_emi,
            2
        ),

        highest_interest_debt=(
            highest_interest.name
        ),

        highest_interest_rate=round(
            highest_interest.interest_rate,
            2
        ),

        lowest_interest_debt=(
            lowest_interest.name
        ),

        lowest_interest_rate=round(
            lowest_interest.interest_rate,
            2
        ),

        weighted_average_interest=round(
            weighted_interest,
            2
        ),

        estimated_monthly_interest=round(
            estimated_monthly_interest,
            2
        ),

        debt_to_income_ratio=round(
            debt_to_income_ratio,
            2
        ),

        number_of_debts=len(debts),

        priority_order=priority_order
    )