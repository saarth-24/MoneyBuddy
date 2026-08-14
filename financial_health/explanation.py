def Explanation(
    recommendations: list[str],
    knowledge_base: dict
):

    explanations = []

    explanation_map = knowledge_base["explanations"]

    for recommendation in recommendations:

        explanations.append(
            explanation_map.get(
                recommendation,
                "No specific advice available."
            )
        )

    return explanations