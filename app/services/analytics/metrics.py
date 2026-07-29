from dataclasses import dataclass

@dataclass
class Metric:

    name: str

    description: str

    keywords: list[str]

    handler: str