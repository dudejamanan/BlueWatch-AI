from app.services.network.network_registry import REGISTRY


def match_network(question: str):

    question = question.lower()

    for metric in REGISTRY:

        for keyword in metric.keywords:

            if keyword in question:

                return metric

    return None