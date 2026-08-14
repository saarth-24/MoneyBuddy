from dataclasses import dataclass


@dataclass
class RiskProfile:

    risk_capacity: str
    risk_tolerance: str
    overall_profile: str

    emergency_months: float
    debt_burden: float
    savings_ratio: float

    explanation: str


def calculate_risk_profile(
    monthly_income: float,
    essential_expenses: float,
    emi: float,
    emergency_fund: float,
    savings_ratio: float,
    debt_ratio: float,
    investment_experience: str = "UNKNOWN"
) -> RiskProfile:

    # -----------------------------------------
    # EMERGENCY COVERAGE
    # -----------------------------------------

    obligations = (
        essential_expenses + emi
    )

    if obligations > 0:
        emergency_months = (
            emergency_fund / obligations
        )
    else:
        emergency_months = 0.0

    # -----------------------------------------
    # RISK CAPACITY
    # -----------------------------------------

    if (
        emergency_months >= 6
        and debt_ratio < 20
        and savings_ratio >= 20
    ):
        capacity = "HIGH"

    elif (
        emergency_months >= 3
        and debt_ratio < 35
        and savings_ratio >= 10
    ):
        capacity = "MODERATE"

    else:
        capacity = "LOW"

    # -----------------------------------------
    # RISK TOLERANCE
    # -----------------------------------------

    experience = (
        investment_experience.upper()
    )

    if experience == "HIGH":
        tolerance = "HIGH"

    elif experience == "MEDIUM":
        tolerance = "MODERATE"

    elif experience == "LOW":
        tolerance = "LOW"

    else:
        tolerance = "MODERATE"

    # -----------------------------------------
    # OVERALL PROFILE
    # -----------------------------------------

    if (
        capacity == "HIGH"
        and tolerance == "HIGH"
    ):
        overall = "AGGRESSIVE"

    elif (
        capacity == "LOW"
        or tolerance == "LOW"
    ):
        overall = "CONSERVATIVE"

    else:
        overall = "MODERATE"

    # -----------------------------------------
    # EXPLANATION
    # -----------------------------------------

    explanation = (
        f"Your emergency fund covers approximately "
        f"{emergency_months:.1f} months of financial "
        f"obligations. Your financial risk capacity is "
        f"{capacity.lower()} based on your emergency "
        f"coverage, debt burden and savings capacity. "
        f"Your overall risk profile is "
        f"{overall.lower()}."
    )

    return RiskProfile(
        risk_capacity=capacity,
        risk_tolerance=tolerance,
        overall_profile=overall,
        emergency_months=round(
            emergency_months,
            2
        ),
        debt_burden=round(
            debt_ratio,
            2
        ),
        savings_ratio=round(
            savings_ratio,
            2
        ),
        explanation=explanation
    )