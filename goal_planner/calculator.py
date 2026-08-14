import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from goal_planner.models import GoalAnalysis


def calculate_goal(
    target_amount: float,
    current_amount: float,
    time_period_years: float,
    monthly_available_for_goal: float
) -> GoalAnalysis:

    # -----------------------------------
    # 1. Calculate remaining amount
    # -----------------------------------

    remaining_amount = max(
        0,
        target_amount - current_amount
    )

    # -----------------------------------
    # 2. Convert years to months
    # -----------------------------------

    months_remaining = int(
        time_period_years * 12
    )

    # -----------------------------------
    # 3. Avoid division by zero
    # -----------------------------------

    if months_remaining <= 0:
        return GoalAnalysis(
            target_amount=target_amount,
            current_amount=current_amount,
            remaining_amount=remaining_amount,
            months_remaining=0,
            required_monthly_saving=0,
            status="INVALID_TIME_PERIOD"
        )

    # -----------------------------------
    # 4. Required monthly contribution
    # -----------------------------------

    required_monthly_saving = (
        remaining_amount / months_remaining
    )

    # -----------------------------------
    # 5. Determine goal status
    # -----------------------------------

    if remaining_amount == 0:

        status = "COMPLETED"

    elif monthly_available_for_goal >= required_monthly_saving:

        status = "ON_TRACK"

    else:

        status = "AT_RISK"

    return GoalAnalysis(
        target_amount=target_amount,
        current_amount=current_amount,
        remaining_amount=remaining_amount,
        months_remaining=months_remaining,
        required_monthly_saving=round(
            required_monthly_saving,
            2
        ),
        status=status
    )






if __name__ == "__main__":

    result = calculate_goal(
        target_amount=1000000,
        current_amount=100000,
        time_period_years=5,
        monthly_available_for_goal=20000
    )

    print("\n==============================")
    print("      GOAL ANALYSIS")
    print("==============================")

    print(f"Target Amount          : ₹{result.target_amount}")
    print(f"Current Amount         : ₹{result.current_amount}")
    print(f"Remaining Amount       : ₹{result.remaining_amount}")
    print(f"Months Remaining       : {result.months_remaining}")
    print(
        f"Required Monthly Saving: "
        f"₹{result.required_monthly_saving}"
    )
    print(f"Status                 : {result.status}")

    print("==============================\n")