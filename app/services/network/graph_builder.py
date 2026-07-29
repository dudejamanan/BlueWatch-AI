import networkx as nx

from app.database.models.accused import Accused


def build_graph(db):

    graph = nx.Graph()

    rows = db.query(
        Accused.CaseMasterID,
        Accused.PersonID,
        Accused.AccusedName
    ).all()

    cases = {}

    for row in rows:

        cases.setdefault(row.CaseMasterID, [])

        cases[row.CaseMasterID].append(
            (row.PersonID, row.AccusedName)
        )

    for accuseds in cases.values():

        for person, name in accuseds:

            graph.add_node(
                person,
                name=name
            )

        for i in range(len(accuseds)):

            for j in range(i + 1, len(accuseds)):

                graph.add_edge(
                    accuseds[i][0],
                    accuseds[j][0]
                )

    return graph