from dataclasses import dataclass


@dataclass
class PortfolioRecommendation:

    action: str
    priority: str
    reason: str

    concentration: float
    risk: str
    diversification: str


def recommend_portfolio_action(
    concentration: float,
    risk: str,
    diversification: str
) -> PortfolioRecommendation:

    # -----------------------------------------
    # HIGH CONCENTRATION
    # -----------------------------------------

    if concentration >= 75:

        return PortfolioRecommendation(

            action=(
                "Avoid increasing the concentrated "
                "position and gradually improve "
                "diversification."
            ),

            priority="HIGH",

            reason=(
                f"Your largest holding represents "
                f"{concentration:.1f}% of the portfolio. "
                f"This creates significant concentration "
                f"risk."
            ),

            concentration=concentration,

            risk=risk,

            diversification=diversification
        )

    # -----------------------------------------
    # MODERATE CONCENTRATION
    # -----------------------------------------

    if concentration >= 50:

        return PortfolioRecommendation(

            action=(
                "Review portfolio diversification "
                "before making additional concentrated "
                "investments."
            ),

            priority="MEDIUM",

            reason=(
                f"Your largest holding represents "
                f"{concentration:.1f}% of the portfolio."
            ),

            concentration=concentration,

            risk=risk,

            diversification=diversification
        )

    # -----------------------------------------
    # NORMAL
    # -----------------------------------------

    return PortfolioRecommendation(

        action=(
            "Maintain diversification and review "
            "portfolio periodically."
        ),

        priority="LOW",

        reason=(
            "No major concentration issue was "
            "detected from the supplied portfolio data."
        ),

        concentration=concentration,

        risk=risk,

        diversification=diversification
    )