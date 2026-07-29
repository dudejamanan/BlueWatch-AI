import networkx as nx

from app.services.network.graph_builder import build_graph


class CrimeNetwork:

    @staticmethod
    def associate_network(db, person_id):

        graph = build_graph(db)

        if person_id not in graph:

            return []

        associates = []

        for neighbour in graph.neighbors(person_id):

            associates.append({

                "person_id": neighbour,

                "name": graph.nodes[neighbour]["name"]

            })

        return associates

    @staticmethod
    def most_connected(db):

        graph = build_graph(db)

        degree = graph.degree()

        result = []

        for node, deg in degree:

            result.append({

                "person_id": node,

                "name": graph.nodes[node]["name"],

                "connections": deg

            })

        result.sort(

            key=lambda x: x["connections"],

            reverse=True

        )

        return result[:10]

    @staticmethod
    def repeat_groups(db):

        graph = build_graph(db)

        groups = list(

            nx.connected_components(graph)

        )

        output = []

        for group in groups:

            if len(group) > 1:

                output.append(list(group))

        return output