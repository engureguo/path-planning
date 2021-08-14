# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt
import graph


# 绘制 graph 中的地图

def draw_graph_with_matplotlib(gra):  # 绘制点之间的邻接关系
    edgelist = []
    labels = {}
    for i in range(len(gra)):
        for j in range(len(gra[i])):
            if gra[i][j] != 0:
                edgelist.append((i, j))
                labels[(i, j)] = gra[i][j]
    point = [i for i in range(graph.PLACES_NUM)]

    print(len(labels))

    G = nx.Graph(edgelist)
    position = nx.circular_layout(G)
    nx.draw_networkx_nodes(G, position, nodelist=point, node_color="r")
    nx.draw_networkx_edges(G, position)
    nx.draw_networkx_labels(G, position)
    nx.draw_networkx_edge_labels(G, position, edge_labels=labels)
    plt.show()


if __name__ == '__main__':
    gra = graph.init_graph().get()
    draw_graph_with_matplotlib(gra)
    # print(gra)
