from types import SimpleNamespace

from ai_cfo.advisor import generate_cfo_advice


def make_decision(category, amount, priority):
    return SimpleNamespace(
        priority=priority,
        category=category,
        action=f"Test {category}",
        recommended_amount=amount,
        allocated_amount=amount,
        reason="Test decision",
        confidence=90.0
    )


def make_investment(amount=0.0):
    return SimpleNamespace(
        action="HOLD",
        recommended_amount=amount,
        reason="Test investment decision",
        confidence=90.0
    )


def make_goal(status="AT_RISK"):
    return SimpleNamespace(
        target_amount=500000.0,
        current_amount=100000.0,
        remaining_amount=400000.0,
        required_monthly_saving=6666.67,
        status=status
    )


def make_health():
    metrics = SimpleNamespace(
        savingratio=4.0,
        expenseratio=70.0,
        debtratio=26.0
    )

    return SimpleNamespace(
        score=75.0,
        metrics=metrics
    )


def make_salary_plan():
    return SimpleNamespace(
        emergency_fund=900.0,
        debt_payment=900.0,
        investments=0.0,
        goal_savings=0.0,
        leisure=200.0
    )


def make_profile():
    return SimpleNamespace(
        salary=50000.0,
        essential_expense=35000.0,
        emi=13000.0,
        debt=250000.0,
        interest=24.0,
        emergency_fund=20000.0,
        goal=500000.0,
        goal_current_amount=100000.0,
        goal_time_period=5
    )


def make_market():
    return SimpleNamespace(
        symbol="INFY",
        current_price=1175.0,
        return_percent=12.2,
        volatility_percent=1.86,
        trend="UPTREND",
        risk_level="MODERATE",
        momentum="POSITIVE"
    )


def make_risk():
    return SimpleNamespace(
        risk_capacity="LOW",
        risk_tolerance="MODERATE",
        overall_profile="CONSERVATIVE",
        emergency_months=0.42,
        explanation="Low risk capacity."
    )


def make_portfolio():
    return SimpleNamespace(
        action="Reduce concentration",
        priority="HIGH",
        reason="Portfolio is highly concentrated."
    )


def make_scenario():
    return SimpleNamespace(
        scenario_name="Current Financial Position",
        monthly_income=50000.0,
        monthly_expenses=35000.0,
        monthly_surplus=2000.0,
        debt_payment=13000.0,
        investment_capacity=2000.0,
        emergency_months=0.42,
        remaining_debt=250000.0,
        goal_status="AT_RISK",
        explanation="Current financial position."
    )


def run_test(name, profile, decisions):
    print("\n----------------------------------------")
    print(f"TEST : {name}")
    print("----------------------------------------")

    try:
        result = generate_cfo_advice(
            user=profile,
            health_advice=make_health(),
            salary_plan=make_salary_plan(),
            goal_analysis=make_goal(),
            market_analysis=make_market(),
            investment_decision=make_investment(),
            decisions=decisions,
            risk_profile=make_risk(),
            goal_priorities=[],
            portfolio_recommendation=make_portfolio(),
            scenario=make_scenario(),
            what_if_scenarios=[]
        )

        print("PASS")
        return True

    except Exception as e:
        print("FAIL")
        print("Reason:", e)
        return False


def main():

    profile = make_profile()

    tests = [
        (
            "Normal financial profile",
            [
                make_decision("EMERGENCY_FUND", 900.0, 1),
                make_decision("DEBT", 900.0, 2),
                make_decision("GOAL", 0.0, 3),
                make_decision("PORTFOLIO", 0.0, 4)
            ]
        ),

        (
            "Zero surplus profile",
            [
                make_decision("EMERGENCY_FUND", 0.0, 1),
                make_decision("DEBT", 0.0, 2),
                make_decision("GOAL", 0.0, 3),
                make_decision("PORTFOLIO", 0.0, 4)
            ]
        ),

        (
            "No investment allocation",
            [
                make_decision("EMERGENCY_FUND", 900.0, 1),
                make_decision("DEBT", 900.0, 2),
                make_decision("GOAL", 0.0, 3),
                make_decision("PORTFOLIO", 0.0, 4)
            ]
        )
    ]

    passed = 0

    for name, decisions in tests:

        if run_test(
            name,
            profile,
            decisions
        ):
            passed += 1

    print("\n========================================")
    print("       EDGE CASE TEST RESULTS")
    print("========================================")

    print(f"Passed : {passed}/{len(tests)}")

    if passed == len(tests):
        print("\nALL EDGE CASE TESTS PASSED")
    else:
        print("\nEDGE CASE TESTS FAILED")

    print("========================================")


if __name__ == "__main__":
    main()