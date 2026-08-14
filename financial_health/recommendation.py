from financial_health.models import Calculations


def Recommendations(
    metrics: Calculations,
    knowledge_base: dict
):

    recommendation = []

    if (
        metrics.savingratio
        < knowledge_base["thresholds"]["savingratio"]
    ):
        recommendation.append("INCREASE_SAVINGS")

    if (
        metrics.expenseratio
        > knowledge_base["thresholds"]["expenseratio"]
    ):
        recommendation.append("REDUCE_EXPENSES")

    if (
        metrics.debtratio
        > knowledge_base["thresholds"]["debtratio"]
    ):
        recommendation.append("REDUCE_DEBT")

    if not recommendation:
        recommendation.append("MAINTAIN_STRATEGY")

    return recommendation