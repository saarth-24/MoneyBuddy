from types import SimpleNamespace

from ai_cfo.advisor import generate_cfo_advice


def obj(**kwargs):
    return SimpleNamespace(**kwargs)


def health(score=75.0, savings=4.0, expenses=70.0, debt=26.0):
    return obj(
        score=score,
        metrics=obj(
            savingratio=savings,
            expenseratio=expenses,
            debtratio=debt,
        ),
    )


def salary_plan():
    return obj(
        emergency_fund=900.0,
        debt_payment=900.0,
        investments=0.0,
        goal_savings=0.0,
        leisure=200.0,
    )


def goal(status="AT_RISK"):
    return obj(
        target_amount=500000.0,
        current_amount=100000.0,
        remaining_amount=400000.0,
        required_monthly_saving=6666.67,
        status=status,
    )


def market():
    return obj(
        symbol="INFY",
        current_price=1175.0,
        return_percent=12.2,
        volatility_percent=1.86,
        trend="UPTREND",
        risk_level="MODERATE",
        momentum="POSITIVE",
    )


def investment(amount=0.0):
    return obj(
        action="HOLD",
        recommended_amount=amount,
        reason="Test investment decision.",
        confidence=95.0,
    )


def risk_profile():
    return obj(
        risk_capacity="LOW",
        risk_tolerance="MODERATE",
        overall_profile="CONSERVATIVE",
        emergency_months=0.42,
        explanation="Test risk profile.",
    )


def portfolio():
    return obj(
        action="Reduce concentration.",
        priority="HIGH",
        reason="Portfolio concentration is high.",
    )


def scenario():
    return obj(
        scenario_name="Current Financial Position",
        monthly_income=50000.0,
        monthly_expenses=35000.0,
        monthly_surplus=2000.0,
        debt_payment=13000.0,
        investment_capacity=2000.0,
        emergency_months=0.42,
        remaining_debt=250000.0,
        goal_status="AT_RISK",
        explanation="Current financial position.",
    )


def decisions(emergency=900.0, debt=900.0, goal_amount=0.0):
    return [
        obj(
            priority=1,
            category="EMERGENCY_FUND",
            action="Build emergency fund",
            recommended_amount=emergency,
            allocated_amount=emergency,
            reason="Build emergency buffer.",
            confidence=90.0,
        ),
        obj(
            priority=2,
            category="DEBT",
            action="Prioritize highest-interest debt repayment",
            recommended_amount=debt,
            allocated_amount=debt,
            reason="Reduce high-interest debt.",
            confidence=95.0,
        ),
        obj(
            priority=3,
            category="GOAL",
            action="Increase goal contribution",
            recommended_amount=6666.67,
            allocated_amount=goal_amount,
            reason="Fund the goal.",
            confidence=85.0,
        ),
    ]


def user(
    salary=50000.0,
    expenses=35000.0,
    emi=13000.0,
    debt=250000.0,
    interest=24.0,
    emergency=20000.0,
):
    return obj(
        salary=salary,
        essential_expense=expenses,
        emi=emi,
        debt=debt,
        interest=interest,
        emergency_fund=emergency,
        goal=500000.0,
        goal_current_amount=100000.0,
        goal_time_period=5,
    )


def run_case(name, **kwargs):

    print()
    print("----------------------------------------")
    print(f"TEST : {name}")
    print("----------------------------------------")

    try:

        result = generate_cfo_advice(
            user=kwargs["user"],
            health_advice=kwargs["health"],
            salary_plan=salary_plan(),
            goal_analysis=goal(),
            market_analysis=market(),
            investment_decision=investment(),
            decisions=kwargs["decisions"],
            risk_profile=risk_profile(),
            goal_priorities=[],
            portfolio_recommendation=portfolio(),
            scenario=scenario(),
            what_if_scenarios=[],
        )

        print("PASS")
        print(
            f"Top Priority : "
            f"{result.top_priority.category}"
        )
        print(
            f"Investment : "
            f"₹{result.investment_amount:.2f}"
        )
        print(
            f"Goal Status : "
            f"{result.goal_status}"
        )

        return True

    except Exception as error:

        print("FAIL")
        print(error)
        return False


def main():

    cases = [

        (
            "Normal profile",
            user(),
            health(),
            decisions(),
        ),

        (
            "Zero emergency fund",
            user(emergency=0.0),
            health(),
            decisions(),
        ),

        (
            "Zero debt",
            user(
                debt=0.0,
                interest=0.0,
                emi=0.0,
            ),
            health(
                debt=0.0
            ),
            decisions(
                emergency=1000.0,
                debt=0.0,
            ),
        ),

        (
            "Zero surplus",
            user(
                expenses=37000.0,
                emi=13000.0,
            ),
            health(),
            decisions(
                emergency=0.0,
                debt=0.0,
            ),
        ),

        (
            "No current investment allocation",
            user(),
            health(),
            decisions(),
        ),

    ]

    passed = 0

    for name, profile, health_data, decision_data in cases:

        if run_case(
            name,
            user=profile,
            health=health_data,
            decisions=decision_data,
        ):
            passed += 1

    print()
    print("========================================")
    print("       FINAL EDGE CASE RESULTS")
    print("========================================")
    print(
        f"Passed : {passed}/{len(cases)}"
    )

    if passed == len(cases):
        print()
        print("ALL FINAL EDGE CASES PASSED")
    else:
        print()
        print("SOME FINAL EDGE CASES FAILED")

    print("========================================")


if __name__ == "__main__":
    main()