import json
import networkx as nx
import matplotlib.pyplot as plt

from networkx.readwrite import json_graph


def read_json_file(filename):
    with open(filename, "r") as f:
        js_graph = json.load(f)
        routes = {}
        for r in js_graph.items():
            routes[r[0]] = json_graph.node_link_graph(r[1])
    return routes


if __name__ == "__main__":

    in_f = "main_test/test_3_route_nets.json"

    g = read_json_file(in_f)

    for r in g.items():
        print(r[0], ":", r[1].nodes)
        nx.draw_spring(r[1], with_labels=True)
        # plt.draw()
        # plt.show()
