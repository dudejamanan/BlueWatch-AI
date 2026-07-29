from decimal import Decimal


def serialize(result):
    """
    Convert SQLAlchemy results into JSON serializable objects.
    """

    if result is None:
        return None

    # Single scalar
    if isinstance(result, (int, float, str, bool)):
        return result

    if isinstance(result, Decimal):
        return float(result)

    # SQLAlchemy Row list
    if isinstance(result, list):

        data = []

        for row in result:

            if hasattr(row, "_mapping"):
                item = {}

                for key, value in row._mapping.items():

                    if isinstance(value, Decimal):
                        value = float(value)

                    item[key] = value

                data.append(item)

            else:
                data.append(row)

        return data

    return result
from decimal import Decimal


def format_result(metric, result):

    data = []

    if isinstance(result, list):

        for row in result:

            if hasattr(row, "_mapping"):

                item = {}

                for key, value in row._mapping.items():

                    if isinstance(value, Decimal):
                        value = int(value)

                    item[key] = value

                data.append(item)

            else:
                data.append(row)

    else:
        data = result

    return {
        "metric": metric.name,
        "description": metric.description,
        "data": data
    }