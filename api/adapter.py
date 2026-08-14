from api.schemas import FinancialProfileRequest
from user_profile.models import (
    FinancialProfile,
    Debt,
    Investment,
    FinancialGoal,
)


def build_financial_profile(
    profile: FinancialProfileRequest
) -> FinancialProfile:
    """
    Converts the backend/API request into MoneyBuddy's
    internal FinancialProfile model.

    The API layer is responsible only for translating
    external input into the internal data structure.
    """

    # =====================================================
    # EXPENSES
    # =====================================================

    # User's total monthly expense is the source of truth.
    #
    # We keep the detailed categories as discretionary/
    # essential information for future use, but we do not
    # double-count them.

    essential_expenses = (
        profile.rent
        + profile.subscriptions_bills
        + profile.household
        + profile.family_dependencies_expense
    )

    # Lifestyle spending is discretionary.
    discretionary_expenses = profile.lifestyle

    # If the detailed categories do not add up to the
    # user's declared total expense, preserve the remaining
    # amount as discretionary spending.
    calculated_expenses = (
        essential_expenses
        + discretionary_expenses
    )

    if profile.total_expense > calculated_expenses:
        discretionary_expenses += (
            profile.total_expense
            - calculated_expenses
        )

    # Never allow calculated expenses to exceed the
    # user's declared total expense because that would
    # artificially reduce the user's surplus.
    elif profile.total_expense < calculated_expenses:
        total_expense = profile.total_expense

        if total_expense >= essential_expenses:
            discretionary_expenses = (
                total_expense
                - essential_expenses
            )
        else:
            # If the supplied category values themselves
            # exceed total expense, cap essential expenses.
            essential_expenses = total_expense
            discretionary_expenses = 0.0

    # =====================================================
    # DEBT
    # =====================================================

    debts = []

    if profile.remaining_principal > 0:

        debts.append(
            Debt(
                name=profile.loan_category
                if profile.loan_category
                else "Loan",

                outstanding=profile.remaining_principal,

                interest_rate=profile.interest_rate,

                emi=profile.loan_emi,

                remaining_months=int(
                    profile.loan_time_period * 12
                )
            )
        )

    # =====================================================
    # INVESTMENT PORTFOLIO
    # =====================================================

    investments = []

    for holding in profile.portfolio:

        investments.append(
            Investment(
                name=holding.symbol,

                asset_type="INVESTMENT",

                current_value=holding.current_value,

                invested_amount=holding.invested_amount
            )
        )

    # =====================================================
    # GOAL
    # =====================================================

    goals = []

    if profile.goal_amount > 0:

        goals.append(
            FinancialGoal(
                name=profile.goal,

                target_amount=profile.goal_amount,

                current_amount=profile.goal_current_amount,

                target_months=int(
                    profile.goal_time_period * 12
                ),

                priority=1
            )
        )

    # =====================================================
    # FINAL INTERNAL PROFILE
    # =====================================================

    return FinancialProfile(

    monthly_income=profile.monthly_income,

    essential_expenses=essential_expenses,

    discretionary_expenses=discretionary_expenses,

    emergency_fund=profile.emergency_fund,

    user_risk_capacity=profile.risk_taking_capacity,

    debts=debts,

    investments=investments,

    goals=goals
)


def build_moneybuddy_user(
    profile: FinancialProfileRequest
):
    """
    Compatibility helper.

    Converts the API request into the existing MoneyBuddy
    User model through the internal FinancialProfile model.
    """

    from user_profile.adapter import profile_to_user

    financial_profile = build_financial_profile(
        profile
    )

    return profile_to_user(
        financial_profile
    )