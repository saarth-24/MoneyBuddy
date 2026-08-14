from user_profile.models import FinancialProfile

from investment_planner.models import (
    InvestmentAnalysis,
    HoldingAnalysis
)


def analyze_portfolio(
    profile: FinancialProfile
) -> InvestmentAnalysis:

    investments = profile.investments

    # =====================================================
    # NO INVESTMENTS
    # =====================================================

    if not investments:

        return InvestmentAnalysis(
            total_value=0.0,
            total_invested=0.0,
            total_gain=0.0,
            total_gain_percent=0.0,
            number_of_investments=0,
            concentration_percent=0.0,
            largest_holding="NONE",
            portfolio_risk="NO_INVESTMENTS",
            diversification_status="NO_INVESTMENTS",
            holdings=[]
        )

    # =====================================================
    # BASIC PORTFOLIO VALUES
    # =====================================================

    total_value = sum(
        investment.current_value
        for investment in investments
    )

    total_invested = sum(
        investment.invested_amount
        for investment in investments
    )

    total_gain = (
        total_value
        - total_invested
    )

    if total_invested > 0:

        total_gain_percent = (
            total_gain
            / total_invested
        ) * 100

    else:

        total_gain_percent = 0.0

    # =====================================================
    # LARGEST HOLDING / CONCENTRATION
    # =====================================================

    largest_investment = max(
        investments,
        key=lambda investment:
        investment.current_value
    )

    if total_value > 0:

        concentration_percent = (
            largest_investment.current_value
            / total_value
        ) * 100

    else:

        concentration_percent = 0.0

    # =====================================================
    # HOLDING ANALYSIS
    # =====================================================

    holdings = []

    for investment in investments:

        gain = (
            investment.current_value
            - investment.invested_amount
        )

        if investment.invested_amount > 0:

            gain_percent = (
                gain
                / investment.invested_amount
            ) * 100

        else:

            gain_percent = 0.0

        if total_value > 0:

            portfolio_weight = (
                investment.current_value
                / total_value
            ) * 100

        else:

            portfolio_weight = 0.0

        holdings.append(

            HoldingAnalysis(

                name=investment.name,

                asset_type=investment.asset_type,

                current_value=round(
                    investment.current_value,
                    2
                ),

                invested_amount=round(
                    investment.invested_amount,
                    2
                ),

                gain=round(
                    gain,
                    2
                ),

                gain_percent=round(
                    gain_percent,
                    2
                ),

                portfolio_weight=round(
                    portfolio_weight,
                    2
                )
            )
        )

    # =====================================================
    # PORTFOLIO RISK
    # =====================================================
    #
    # Risk is based primarily on concentration.
    #
    # This prevents a 100% concentrated portfolio from
    # incorrectly being classified as LOW risk simply
    # because the asset type is not "STOCK".
    #

    if concentration_percent >= 75:

        portfolio_risk = "HIGH"

    elif concentration_percent >= 50:

        portfolio_risk = "MODERATE"

    else:

        portfolio_risk = "LOW"

    # =====================================================
    # DIVERSIFICATION
    # =====================================================

    if len(investments) == 1:

        diversification_status = "LOW"

    elif concentration_percent > 50:

        diversification_status = "LOW"

    else:

        diversification_status = "DIVERSIFIED"

    # =====================================================
    # RETURN ANALYSIS
    # =====================================================

    return InvestmentAnalysis(

        total_value=round(
            total_value,
            2
        ),

        total_invested=round(
            total_invested,
            2
        ),

        total_gain=round(
            total_gain,
            2
        ),

        total_gain_percent=round(
            total_gain_percent,
            2
        ),

        number_of_investments=len(
            investments
        ),

        concentration_percent=round(
            concentration_percent,
            2
        ),

        largest_holding=(
            largest_investment.name
        ),

        portfolio_risk=portfolio_risk,

        diversification_status=(
            diversification_status
        ),

        holdings=holdings
    )