from app.services.analytics.registry import REGISTRY


def match_metric(question: str):

    question = question.lower()

    # 1. Exact substring match
    for metric in REGISTRY:
        for keyword in metric.keywords:
            if keyword.lower() in question:
                return metric

    # 2. Word-overlap fallback
    best_metric = None
    best_score = 0

    question_words = set(question.split())

    for metric in REGISTRY:

        for keyword in metric.keywords:

            keyword_words = set(keyword.lower().split())

            score = len(question_words.intersection(keyword_words))

            if score > best_score:
                best_score = score
                best_metric = metric

    if best_score == 0:
        return None

    return best_metric