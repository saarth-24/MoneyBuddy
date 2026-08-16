from financial_health.models import User
from user_profile.models import FinancialProfile


def profile_to_user(profile: FinancialProfile) -> User:
    """
    Converts the new FinancialProfile into the existing
    User model used by MoneyBuddy's current financial engine.

    This is a compatibility layer. It allows us to upgrade
    the data model without rewriting every existing module.
    """

    # -----------------------------
    # TOTAL DEBT
    # -----------------------------

    total_debt = profile.total_debt

    # -----------------------------
    # TOTAL EMI
    # -----------------------------

    total_emi = profile.monthly_emi

    # -----------------------------
    # HIGHEST INTEREST RATE
    # -----------------------------

    if profile.debts:

        highest_interest_debt = max(
            profile.debts,
            key=lambda debt: debt.interest_rate
        )

        interest_rate = (
            highest_interest_debt.interest_rate
        )

        loan_time_period = (
            highest_interest_debt.remaining_months / 12
        )

    else:

        interest_rate = 0.0
        loan_time_period = 0.0

    # -----------------------------
    # PRIMARY GOAL
    # -----------------------------

    if profile.goals:

        primary_goal = min(
            profile.goals,
            key=lambda goal: goal.priority
        )

        goal_amount = primary_goal.target_amount

        goal_time_period = (
            primary_goal.target_months / 12
        )

        current_goal_amount = (
            primary_goal.current_amount
        )

    else:

        goal_amount = 0.0
        goal_time_period = 0.0
        current_goal_amount = 0.0

    # -----------------------------
    # TOTAL EXPENSE
    # -----------------------------

    total_expense = (
        profile.essential_expenses
        + profile.discretionary_expenses
    )

    # -----------------------------
    # EXISTING USER MODEL
    # -----------------------------

    return User(
    salary=profile.monthly_income,

    essential_expense=(
        total_expense
    ),

        debt=total_debt,

        emi=total_emi,

        interest=interest_rate,

        loan_time_period=loan_time_period,

        emergency_fund=profile.emergency_fund,

        goal=goal_amount,

        goal_time_period=goal_time_period,

        goal_current_amount=current_goal_amount
    )