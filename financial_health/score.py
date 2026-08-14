from financial_health.models import Calculations


def healthscore(
    metrics: Calculations,
    knowledge_base: dict
):

    score = 100.0

    if (
        metrics.savingratio
        < knowledge_base["thresholds"]["savingratio"]
    ):
        score -= knowledge_base["penalty"]["savingratiopenalty"]

    if (
        metrics.expenseratio
        > knowledge_base["thresholds"]["expenseratio"]
    ):
        score -= knowledge_base["penalty"]["expenseratiopenalty"]

    if (
        metrics.debtratio
        > knowledge_base["thresholds"]["debtratio"]
    ):
        score -= knowledge_base["penalty"]["debtratiopenalty"]

    return max(0, score)