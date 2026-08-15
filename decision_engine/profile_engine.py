from dataclasses import dataclass
from typing import List

from user_profile.models import FinancialProfile

from user_profile.debt_analyzer import (
    DebtAnalysis
)

from user_profile.goal_analyzer import (
    GoalsAnalysis
)

from investment_planner.models import (
    InvestmentAnalysis
)


@dataclass
class RankedDecision:

    priority: int
    category: str
    action: str

    recommended_amount: float

    reason: str
    confidence: float


def make_profile_decisions(

    profile: FinancialProfile,

    debt_analysis: DebtAnalysis,

    goals_analysis: GoalsAnalysis,

    portfolio_analysis: InvestmentAnalysis

) -> List[RankedDecision]:

    decisions = []

    # =========================================
    # MONTHLY SURPLUS
    # =========================================

    monthly_surplus = (
        profile.monthly_income
        - profile.essential_expenses
        - debt_analysis.total_emi
    )

    monthly_surplus = max(
        monthly_surplus,
        0.0
    )

    # =========================================
    # EMERGENCY FUND
    # =========================================

    monthly_obligations = (
        profile.essential_expenses
        + debt_analysis.total_emi
    )

    if monthly_obligations > 0:

        emergency_months = (
            profile.emergency_fund
            / monthly_obligations
        )

    else:

        emergency_months = 0.0

    if emergency_months < 3:

        emergency_allocation = (
            monthly_surplus * 0.45
        )

        decisions.append(

            RankedDecision(

                priority=1,

                category="EMERGENCY_FUND",

                action="Build emergency fund",

                recommended_amount=round(
                    emergency_allocation,
                    2
                ),

                reason=(
                    f"Your emergency fund currently "
                    f"covers only {emergency_months:.1f} "
                    f"months of essential financial "
                    f"obligations."
                ),

                confidence=90.0
            )
        )

    # =========================================
    # HIGH INTEREST DEBT
    # =========================================

    if (
        debt_analysis.number_of_debts > 0
        and
        debt_analysis.highest_interest_rate >= 12
    ):

        debt_allocation = (
            monthly_surplus * 0.45
        )

        decisions.append(

            RankedDecision(

                priority=2,

                category="DEBT",

                action=(
                    "Prioritize highest-interest "
                    "debt repayment"
                ),

                recommended_amount=round(
                    debt_allocation,
                    2
                ),

                reason=(
                    f"{debt_analysis.highest_interest_debt} "
                    f"has the highest interest rate at "
                    f"{debt_analysis.highest_interest_rate:.2f}%. "
                    f"Reducing expensive debt can "
                    f"potentially reduce future interest "
                    f"costs, subject to the loan terms."
                ),

                confidence=95.0
            )
        )

    # =========================================
    # GOAL
    # =========================================

    if goals_analysis.total_goals > 0:

        highest_goal = (
            goals_analysis.goals[0]
        )

        if (
            highest_goal.required_monthly_saving
            > monthly_surplus
    ):

            decisions.append(

                RankedDecision(

                    priority=3,

                    category="GOAL",

                    action=(
                        "Increase goal contribution "
                        "when higher-priority "
                        "obligations are under control"
                    ),

                    recommended_amount=0.0,

                    reason=(
                        f"{highest_goal.name} requires "
                        f"approximately ₹"
                        f"{highest_goal.required_monthly_saving:.2f} "
                        f"per month, but available "
                        f"monthly surplus is only "
                        f"₹{monthly_surplus:.2f}."
                    ),

                    confidence=85.0
                )
            )

    # =========================================
    # PORTFOLIO CONCENTRATION
    # =========================================

    if (
        portfolio_analysis.number_of_investments > 0
        and
        portfolio_analysis.concentration_percent > 50
    ):

        decisions.append(

            RankedDecision(

                priority=4,

                category="PORTFOLIO",

                action="Reduce portfolio concentration",

                recommended_amount=0.0,

                reason=(
                    f"{portfolio_analysis.largest_holding} "
                    f"represents "
                    f"{portfolio_analysis.concentration_percent:.1f}% "
                    f"of your portfolio."
                ),

                confidence=90.0
            )
        )

    # =========================================
    # INVESTMENT
    # =========================================

    if (
        monthly_surplus > 0
        and
        emergency_months >= 3
        and
        (
            debt_analysis.number_of_debts == 0
            or
            debt_analysis.highest_interest_rate < 12
        )
    ):

        investment_amount = (
            monthly_surplus * 0.20
        )

        decisions.append(

            RankedDecision(

                priority=5,

                category="INVESTMENT",

                action="Invest available surplus",

                recommended_amount=round(
                    investment_amount,
                    2
                ),

                reason=(
                    "Your emergency reserve and "
                    "high-interest debt position "
                    "allow consideration of "
                    "additional investment."
                ),

                confidence=75.0
            )
        )

    # =========================================
    # SORT
    # =========================================

    decisions.sort(
        key=lambda decision:
        decision.priority
    )

    # Re-number priorities

    for index, decision in enumerate(
        decisions,
        start=1
    ):

        decision.priority = index

    return decisions