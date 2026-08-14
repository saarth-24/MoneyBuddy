from risk_engine.profiler import (
    calculate_risk_profile
)


profile = calculate_risk_profile(

    monthly_income=50000,

    essential_expenses=35000,

    emi=13000,

    emergency_fund=20000,

    savings_ratio=4,

    debt_ratio=26,

    investment_experience="LOW"
)


print("\n==============================")
print("MONEYBUDDY RISK PROFILE")
print("==============================")

print(
    f"Risk Capacity : "
    f"{profile.risk_capacity}"
)

print(
    f"Risk Tolerance : "
    f"{profile.risk_tolerance}"
)

print(
    f"Overall Profile : "
    f"{profile.overall_profile}"
)

print(
    f"Emergency Coverage : "
    f"{profile.emergency_months} months"
)

print(
    f"\nExplanation:\n"
    f"{profile.explanation}"
)