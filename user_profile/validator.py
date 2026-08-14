from user_profile.models import FinancialProfile


def validate_profile(profile: FinancialProfile) -> None:

    if profile.monthly_income <= 0:
        raise ValueError(
            "Monthly income must be greater than zero."
        )

    if profile.essential_expenses < 0:
        raise ValueError(
            "Essential expenses cannot be negative."
        )

    if profile.discretionary_expenses < 0:
        raise ValueError(
            "Discretionary expenses cannot be negative."
        )

    if profile.emergency_fund < 0:
        raise ValueError(
            "Emergency fund cannot be negative."
        )

    for debt in profile.debts:

        if debt.outstanding < 0:
            raise ValueError(
                f"Outstanding debt cannot be negative: {debt.name}"
            )

        if debt.interest_rate < 0:
            raise ValueError(
                f"Interest rate cannot be negative: {debt.name}"
            )

        if debt.emi < 0:
            raise ValueError(
                f"EMI cannot be negative: {debt.name}"
            )

        if debt.remaining_months < 0:
            raise ValueError(
                f"Remaining months cannot be negative: {debt.name}"
            )

    for investment in profile.investments:

        if investment.current_value < 0:
            raise ValueError(
                f"Investment value cannot be negative: "
                f"{investment.name}"
            )

        if investment.invested_amount < 0:
            raise ValueError(
                f"Invested amount cannot be negative: "
                f"{investment.name}"
            )

    for goal in profile.goals:

        if goal.target_amount <= 0:
            raise ValueError(
                f"Goal target must be greater than zero: "
                f"{goal.name}"
            )

        if goal.current_amount < 0:
            raise ValueError(
                f"Goal current amount cannot be negative: "
                f"{goal.name}"
            )

        if goal.target_months <= 0:
            raise ValueError(
                f"Goal target period must be greater than zero: "
                f"{goal.name}"
            )