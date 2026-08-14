from dataclasses import asdict, is_dataclass
from typing import Any


# =========================================================
# GENERIC SERIALIZER
# =========================================================

def _serialize(value: Any):
    """
    Convert MoneyBuddy dataclasses and nested objects
    into JSON-safe Python structures.
    """

    if is_dataclass(value):
        return {
            key: _serialize(val)
            for key, val in asdict(value).items()
        }

    if isinstance(value, list):
        return [
            _serialize(item)
            for item in value
        ]

    if isinstance(value, tuple):
        return [
            _serialize(item)
            for item in value
        ]

    if isinstance(value, dict):
        return {
            key: _serialize(val)
            for key, val in value.items()
        }

    if isinstance(value, (str, int, float, bool)) or value is None:
        return value

    if hasattr(value, "__dict__"):
        return {
            key: _serialize(val)
            for key, val in vars(value).items()
        }

    return str(value)


# =========================================================
# SAFE FLOAT
# =========================================================

def _float(value, default=0.0):
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


# =========================================================
# FINANCIAL HEALTH
# =========================================================

def _build_financial_health(health):
    if health is None:
        return None

    if hasattr(health, "metrics") and health.metrics is not None:
        metrics = health.metrics
        return {
            "savingratio": _float(getattr(metrics, "savingratio", 0.0)),
            "expenseratio": _float(getattr(metrics, "expenseratio", 0.0)),
            "debtratio": _float(getattr(metrics, "debtratio", 0.0)),
            "score": _float(getattr(health, "score", 0.0)),
            "recommendation": _serialize(getattr(health, "recommendation", [])),
            "explanation": _serialize(getattr(health, "explanation", [])),
        }
    elif isinstance(health, dict):
        metrics = health.get("metrics", {})
        if isinstance(metrics, dict):
            return {
                "savingratio": _float(metrics.get("savingratio", 0.0)),
                "expenseratio": _float(metrics.get("expenseratio", 0.0)),
                "debtratio": _float(metrics.get("debtratio", 0.0)),
                "score": _float(health.get("score", 0.0)),
                "recommendation": _serialize(health.get("recommendation", [])),
                "explanation": _serialize(health.get("explanation", [])),
            }

    serialized = _serialize(health)
    if isinstance(serialized, dict):
        metrics = serialized.get("metrics", {})
        if isinstance(metrics, dict):
            return {
                "savingratio": _float(metrics.get("savingratio", 0.0)),
                "expenseratio": _float(metrics.get("expenseratio", 0.0)),
                "debtratio": _float(metrics.get("debtratio", 0.0)),
                "score": _float(serialized.get("score", 0.0)),
                "recommendation": serialized.get("recommendation", []),
                "explanation": serialized.get("explanation", []),
            }
        return serialized

    return None


# =========================================================
# SCENARIOS
# =========================================================

def _build_scenarios(ranked_scenarios):
    if not ranked_scenarios:
        return []

    scenarios = []
    for item in ranked_scenarios:
        item_data = _serialize(item)
        if isinstance(item_data, dict):
            scenario = item_data.get("scenario")
            scenarios.append({
                "rank": item_data.get("rank"),
                "score": _float(item_data.get("score")),
                "scenario": scenario
            })
        else:
            scenarios.append(item_data)

    return scenarios


# =========================================================
# FINAL API RESPONSE
# =========================================================

def build_api_response(result: dict) -> dict:
    if not isinstance(result, dict):
        raise TypeError("MoneyBuddy engine result must be a dictionary.")

    health = result.get("health_advice")
    goal = result.get("goal_analysis")
    debt = result.get("debt_analysis")
    goals = result.get("goals_analysis")
    portfolio = result.get("portfolio_analysis")
    investment = result.get("investment_decision")
    risk = result.get("risk_profile")
    goal_priorities = result.get("goal_priorities", [])
    portfolio_recommendation = result.get("portfolio_recommendation")
    scenario = result.get("scenario")
    ranked_scenarios = result.get("ranked_scenarios", [])
    best_scenario = result.get("best_scenario")
    action_plan = result.get("action_plan")
    ai_advice = result.get("ai_advice")

    return {
        "financial_health": _build_financial_health(health),
        "goal": _serialize(goal),
        "debt": _serialize(debt),
        "goals_intelligence": _serialize(goals) if goals is not None else {},
        "portfolio": _serialize(portfolio),
        "investment_decision": _serialize(investment),
        "risk_profile": _serialize(risk),
        "goal_priorities": _serialize(goal_priorities) if goal_priorities is not None else [],
        "portfolio_recommendation": _serialize(portfolio_recommendation),
        "current_scenario": _serialize(scenario),
        "what_if_scenarios": _build_scenarios(ranked_scenarios),
        "best_scenario": _serialize(best_scenario) if best_scenario is not None else None,
        "action_plan": _serialize(action_plan),
        "ai_cfo": _serialize(ai_advice)
    }