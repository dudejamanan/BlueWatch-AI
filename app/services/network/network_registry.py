from dataclasses import dataclass


@dataclass
class NetworkMetric:
    name: str
    description: str
    keywords: list[str]
    handler: str


REGISTRY = [

    NetworkMetric(
        name="associate_network",
        description="Find associates of a criminal",
        keywords=[
            "network",
            "associate",
            "connection",
            "linked",
            "relation",
            "gang",
            "accomplice"
        ],
        handler="associate_network"
    ),

    NetworkMetric(
        name="repeat_groups",
        description="Groups repeatedly committing crimes together",
        keywords=[
            "repeat offenders",
            "group",
            "crew",
            "gang"
        ],
        handler="repeat_groups"
    ),

    NetworkMetric(
        name="most_connected",
        description="Most connected criminals",
        keywords=[
            "most connected",
            "central",
            "hub",
            "leader"
        ],
        handler="most_connected"
    ),
]