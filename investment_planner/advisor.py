from dataclasses import dataclass

from financial_health.models import User, Advice
from salary_planner.models import SalaryPlan
from goal_planner.models import GoalAnalysis
from market.analyzer import MarketAnalysis

from investment_planner.models import InvestmentAnalysis


@dataclass
class InvestmentDecision:

    action: str
    recommended_amount: float
    reason: str
    confidence: float


def analyze_investment_opportunity(
    user: User,
    health_advice: Advice,
    salary_plan: SalaryPlan,
    goal_analysis: GoalAnalysis,
    market_analysis: MarketAnalysis,
    portfolio_analysis: InvestmentAnalysis
) -> InvestmentDecision:

    # --------------------------------------------------
    # 1. HIGH-INTEREST DEBT HAS HIGHEST PRIORITY
    # --------------------------------------------------

    if user.debt > 0 and user.interest >= 12:

        return InvestmentDecision(
            action=(
                "Delay aggressive investing and "
                "prioritize high-interest debt"
            ),

            recommended_amount=0.0,

            reason=(
                f"Your existing debt carries a "
                f"{user.interest:.2f}% interest rate. "
                f"Reducing expensive debt should take "
                f"priority over increasing investment "
                f"exposure."
            ),

            confidence=95.0
        )

    # --------------------------------------------------
    # 2. EMERGENCY FUND CHECK
    # --------------------------------------------------

    monthly_expenses = (
        user.essential_expense +
        user.emi
    )

    if monthly_expenses > 0:

        emergency_months = (
            user.emergency_fund /
            monthly_expenses
        )

    else:

        emergency_months = 0

    if emergency_months < 3:

        return InvestmentDecision(
            action="Build emergency fund before investing",

            recommended_amount=0.0,

            reason=(
                f"Your emergency fund currently covers "
                f"only {emergency_months:.1f} months of "
                f"essential financial obligations. "
                f"Building a stronger cash reserve should "
                f"take priority over additional investment risk."
            ),

            confidence=92.0
        )

    # --------------------------------------------------
    # 3. GOAL RISK CHECK
    # --------------------------------------------------

    if goal_analysis.status == "AT_RISK":

        return InvestmentDecision(
            action="Prioritize goal funding before aggressive investing",

            recommended_amount=0.0,

            reason=(
                f"Your financial goal is currently "
                f"{goal_analysis.status}. The required "
                f"monthly contribution is "
                f"₹{goal_analysis.required_monthly_saving:.2f}. "
                f"Additional investment risk should be limited "
                f"until the goal is better funded."
            ),

            confidence=88.0
        )

    # --------------------------------------------------
    # 4. PORTFOLIO CONCENTRATION CHECK
    # --------------------------------------------------

    if portfolio_analysis.concentration_percent > 50:

        return InvestmentDecision(
            action="Avoid increasing concentration in current holdings",

            recommended_amount=0.0,

            reason=(
                f"{portfolio_analysis.largest_holding} represents "
                f"{portfolio_analysis.concentration_percent:.1f}% "
                f"of your current portfolio. Increasing exposure "
                f"to the same holding would increase concentration "
                f"risk."
            ),

            confidence=90.0
        )

    # --------------------------------------------------
    # 5. HIGH PORTFOLIO RISK CHECK
    # --------------------------------------------------

    if portfolio_analysis.portfolio_risk == "HIGH":

        return InvestmentDecision(
            action="Review portfolio risk before increasing investments",

            recommended_amount=0.0,

            reason=(
                "Your current portfolio has a high-risk profile. "
                "MoneyBuddy recommends reviewing diversification "
                "before adding significant new investment exposure."
            ),

            confidence=85.0
        )

    # --------------------------------------------------
    # 6. POSITIVE MARKET + HEALTHY FINANCIAL POSITION
    # --------------------------------------------------

    if (
        market_analysis.momentum == "POSITIVE"
        and
        salary_plan.investments > 0
    ):

        return InvestmentDecision(
            action="Invest available surplus",

            recommended_amount=salary_plan.investments,

            reason=(
                f"The current market signal for "
                f"{market_analysis.symbol} is positive, "
                f"and your financial position allows "
                f"additional investment after higher-priority "
                f"obligations."
            ),

            confidence=75.0
        )

    # --------------------------------------------------
    # 7. DEFAULT
    # --------------------------------------------------

    return InvestmentDecision(
        action="Maintain current investment allocation",

        recommended_amount=salary_plan.investments,

        reason=(
            "Your current financial position does not "
            "support increasing investment exposure at "
            "this time."
        ),

        confidence=70.0
    )