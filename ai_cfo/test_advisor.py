"""
MoneyBuddy AI CFO validation tests.

Run:

    python -m ai_cfo.test_advisor

These tests verify two important properties:

1. Valid Gemini responses are accepted.
2. Invalid Gemini responses are rejected and replaced
   by the deterministic MoneyBuddy financial-engine result.

The AI is NEVER allowed to override the Python engine.
"""

from types import SimpleNamespace

import ai_cfo.advisor as advisor
from ai_cfo.advisor import generate_cfo_advice


# =========================================================
# TEST DATA
# =========================================================

def make_user():
    return SimpleNamespace(
        salary=50000.0,
        essential_expense=35000.0,
        emi=13000.0,
        debt=250000.0,
        interest=24.0,
        emergency_fund=20000.0,
        goal=500000.0,
    )


def make_health():
    metrics = SimpleNamespace(
        savingratio=4.0,
        expenseratio=70.0,
        debtratio=26.0,
    )

    return SimpleNamespace(
        score=75.0,
        metrics=metrics,
    )


def make_salary_plan():
    return SimpleNamespace(
        emergency_fund=900.0,
        debt_payment=900.0,
        investments=0.0,
        goal_savings=0.0,
        leisure=200.0,
    )


def make_goal():
    return SimpleNamespace(
        target_amount=500000.0,
        current_amount=100000.0,
        remaining_amount=400000.0,
        required_monthly_saving=6666.67,
        status="AT_RISK",
    )


def make_market():
    return SimpleNamespace(
        symbol="INFY",
        current_price=1175.0,
        return_percent=12.20,
        volatility_percent=1.86,
        trend="UPTREND",
        risk_level="MODERATE",
        momentum="POSITIVE",
    )


def make_investment():
    return SimpleNamespace(
        action=(
            "Delay aggressive investing and "
            "prioritize high-interest debt"
        ),
        recommended_amount=0.0,
        reason=(
            "Your existing debt carries a 24.00% "
            "interest rate."
        ),
        confidence=95.0,
    )


def make_decisions():
    return [
        SimpleNamespace(
            priority=1,
            category="EMERGENCY_FUND",
            action="Build emergency fund",
            recommended_amount=900.0,
            allocated_amount=900.0,
            reason=(
                "Your emergency fund currently covers "
                "only 0.4 months of essential obligations."
            ),
            confidence=90.0,
        ),

        SimpleNamespace(
            priority=2,
            category="DEBT",
            action="Prioritize highest-interest debt repayment",
            recommended_amount=900.0,
            allocated_amount=900.0,
            reason=(
                "Credit Card has the highest interest "
                "rate at 24.00%."
            ),
            confidence=95.0,
        ),

        SimpleNamespace(
            priority=3,
            category="GOAL",
            action=(
                "Increase goal contribution when "
                "higher-priority obligations are under control"
            ),
            recommended_amount=6666.67,
            allocated_amount=0.0,
            reason=(
                "House Goal requires approximately "
                "₹6666.67 per month."
            ),
            confidence=85.0,
        ),

        SimpleNamespace(
            priority=4,
            category="PORTFOLIO",
            action="Reduce portfolio concentration",
            recommended_amount=0.0,
            allocated_amount=0.0,
            reason=(
                "INFY represents 100.0% of your portfolio."
            ),
            confidence=90.0,
        ),
    ]


def make_risk_profile():
    return SimpleNamespace(
        risk_capacity="LOW",
        risk_tolerance="MODERATE",
        overall_profile="CONSERVATIVE",
        emergency_months=0.42,
        explanation="Conservative risk profile.",
    )


def make_goal_priorities():
    return [
        SimpleNamespace(
            name="House Goal",
            priority_score=41.0,
            urgency="LOW",
            recommended_focus="MEDIUM",
            reason=(
                "House Goal requires approximately "
                "₹6666.67 per month."
            ),
        )
    ]


def make_portfolio_recommendation():
    return SimpleNamespace(
        action=(
            "Avoid increasing the concentrated position "
            "and gradually improve diversification."
        ),
        priority="HIGH",
        reason=(
            "Your largest holding represents 100.0% "
            "of the portfolio."
        ),
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
        explanation="Current financial position.",
    )


# =========================================================
# COMMON ARGUMENTS
# =========================================================

def base_arguments():

    return {
        "user": make_user(),
        "health_advice": make_health(),
        "salary_plan": make_salary_plan(),
        "goal_analysis": make_goal(),
        "market_analysis": make_market(),
        "investment_decision": make_investment(),
        "decisions": make_decisions(),
        "risk_profile": make_risk_profile(),
        "goal_priorities": make_goal_priorities(),
        "portfolio_recommendation":
            make_portfolio_recommendation(),
        "scenario": make_scenario(),
        "what_if_scenarios": [],
    }


# =========================================================
# VALID GEMINI RESPONSE
# =========================================================

def valid_response():

    return {

        "headline":
            "MoneyBuddy Financial Plan",

        "financial_status":
            "Financial stability requires emergency "
            "savings and debt reduction.",

        "top_priority": {

            "category":
                "EMERGENCY_FUND",

            "action":
                "Build emergency fund",

            "amount":
                900.0,

            "reason":
                "Build financial resilience.",
        },

        "secondary_priorities": [

            {
                "category":
                    "DEBT",

                "action":
                    "Prioritize highest-interest debt repayment",

                "amount":
                    900.0,

                "reason":
                    "Reduce expensive debt.",
            },

            {
                "category":
                    "GOAL",

                "action":
                    (
                        "Increase goal contribution when "
                        "higher-priority obligations are "
                        "under control"
                    ),

                "amount":
                    0.0,

                "reason":
                    "Goal currently underfunded.",
            },

            {
                "category":
                    "PORTFOLIO",

                "action":
                    "Reduce portfolio concentration",

                "amount":
                    0.0,

                "reason":
                    "Portfolio is concentrated.",
            },
        ],

        "investment_status":
            "PAUSED",

        "investment_amount":
            0.0,

        "investment_reason":
            "Prioritize high-interest debt.",

        "goal_status":
            "AT_RISK",

        "goal_shortfall":
            6666.67,

        "why": [
            "Emergency fund is low.",
            "Debt interest rate is high.",
        ],

        "next_steps": [
            "Build emergency savings.",
            "Reduce high-interest debt.",
        ],

        "reassessment_triggers": [
            "Income changes.",
            "Debt is significantly reduced.",
        ],

        "personal_message":
            "Focus on financial stability first.",
    }


# =========================================================
# FAKE GEMINI CLIENT
# =========================================================

class FakeClient:

    def __init__(self, response):

        self.response = response

    def generate_advice(
        self,
        system_prompt,
        user_prompt
    ):

        return self.response


class BrokenClient:

    def generate_advice(
        self,
        system_prompt,
        user_prompt
    ):

        raise RuntimeError(
            "Simulated Gemini API failure"
        )


# =========================================================
# RUN ONE TEST
# =========================================================

def run_test(
    name,
    fake_response,
    expected_top_category="EMERGENCY_FUND",
    expected_top_amount=900.0,
    expected_investment_amount=0.0,
    expected_goal_status="AT_RISK",
    expected_goal_shortfall=6666.67,
    expected_secondary_count=3,
):

    print()
    print("----------------------------------------")
    print(f"TEST : {name}")
    print("----------------------------------------")

    original_client = advisor.AICFOClient

    advisor.AICFOClient = lambda: FakeClient(
        fake_response
    )

    try:

        result = generate_cfo_advice(
            **base_arguments()
        )

        # -------------------------------------------------
        # VERIFY FALLBACK / RESULT
        # -------------------------------------------------

        checks = [

            (
                result.top_priority.category
                == expected_top_category,
                "top priority category"
            ),

            (
                abs(
                    result.top_priority.amount
                    - expected_top_amount
                ) < 0.01,
                "top priority amount"
            ),

            (
                abs(
                    result.investment_amount
                    - expected_investment_amount
                ) < 0.01,
                "investment amount"
            ),

            (
                result.goal_status
                == expected_goal_status,
                "goal status"
            ),

            (
                abs(
                    result.goal_shortfall
                    - expected_goal_shortfall
                ) < 0.01,
                "goal shortfall"
            ),

            (
                len(result.secondary_priorities)
                == expected_secondary_count,
                "secondary priority count"
            ),
        ]

        failed_checks = [
            label
            for passed, label in checks
            if not passed
        ]

        if failed_checks:

            print("❌ FAIL")

            print(
                "Incorrect values: "
                + ", ".join(failed_checks)
            )

            return False

        print("✅ PASS")

        return True

    except Exception as error:

        print("❌ FAIL")
        print(error)

        return False

    finally:

        advisor.AICFOClient = original_client


# =========================================================
# MAIN
# =========================================================

def main():

    passed = 0
    total = 0

    # =====================================================
    # 1. VALID RESPONSE
    # =====================================================

    total += 1

    if run_test(
        "Valid Gemini response",
        valid_response()
    ):

        passed += 1

    # =====================================================
    # 2. WRONG TOP PRIORITY
    # =====================================================

    response = valid_response()

    response["top_priority"]["category"] = "DEBT"

    total += 1

    if run_test(
        "Reject wrong top priority and use fallback",
        response
    ):

        passed += 1

    # =====================================================
    # 3. WRONG TOP PRIORITY AMOUNT
    # =====================================================

    response = valid_response()

    response["top_priority"]["amount"] = 5000.0

    total += 1

    if run_test(
        "Reject changed top-priority allocation",
        response
    ):

        passed += 1

    # =====================================================
    # 4. WRONG SECONDARY ALLOCATION
    # =====================================================

    response = valid_response()

    response["secondary_priorities"][0]["amount"] = 5000.0

    total += 1

    if run_test(
        "Reject changed secondary allocation",
        response
    ):

        passed += 1

    # =====================================================
    # 5. WRONG INVESTMENT
    # =====================================================

    response = valid_response()

    response["investment_amount"] = 5000.0

    total += 1

    if run_test(
        "Reject changed investment allocation",
        response
    ):

        passed += 1

    # =====================================================
    # 6. WRONG GOAL STATUS
    # =====================================================

    response = valid_response()

    response["goal_status"] = "ON_TRACK"

    total += 1

    if run_test(
        "Reject changed goal status",
        response
    ):

        passed += 1

    # =====================================================
    # 7. WRONG GOAL SHORTFALL
    # =====================================================

    response = valid_response()

    response["goal_shortfall"] = 1000.0

    total += 1

    if run_test(
        "Reject changed goal shortfall",
        response
    ):

        passed += 1

    # =====================================================
    # 8. MISSING SECONDARY PRIORITY
    # =====================================================

    response = valid_response()

    response["secondary_priorities"] = []

    total += 1

    if run_test(
        "Reject missing secondary priorities",
        response
    ):

        passed += 1

    # =====================================================
    # 9. GEMINI UNAVAILABLE
    # =====================================================

    print()
    print("----------------------------------------")
    print("TEST : Gemini unavailable fallback")
    print("----------------------------------------")

    original_client = advisor.AICFOClient

    advisor.AICFOClient = BrokenClient

    try:

        result = generate_cfo_advice(
            **base_arguments()
        )

        if (
            result.top_priority.category
            == "EMERGENCY_FUND"
            and
            abs(
                result.top_priority.amount
                - 900.0
            ) < 0.01
            and
            result.investment_amount
            == 0.0
        ):

            print("✅ PASS")

            print(
                "Deterministic fallback preserved "
                "the MoneyBuddy engine decisions."
            )

            passed += 1

        else:

            print("❌ FAIL")

    except Exception as error:

        print("❌ FAIL")
        print(error)

    finally:

        advisor.AICFOClient = original_client

    total += 1

    # =====================================================
    # FINAL
    # =====================================================

    print()
    print("========================================")
    print("       AI CFO VALIDATION RESULTS")
    print("========================================")

    print(
        f"Passed : {passed}/{total}"
    )

    if passed == total:

        print()
        print(
            "✅ ALL AI CFO TESTS PASSED"
        )

        print()
        print(
            "MoneyBuddy successfully rejects "
            "AI-generated financial changes and "
            "falls back to the deterministic engine."
        )

    else:

        print()
        print(
            f"❌ {total - passed} TEST(S) FAILED"
        )

    print(
        "========================================"
    )


if __name__ == "__main__":
    main()