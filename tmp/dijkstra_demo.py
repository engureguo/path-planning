# -*- coding: utf-8 -*-
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# 不是 dijkstra 算法
# 绘图
# 邻接关系、边的权值

# 链表
graph_chain = {
    'a': {'b': 7, 'c': 9, 'f': 14},
    'b': {'a': 7, 'c': 10, 'd': 15},
    'c': {'a': 9, 'b': 10, 'd': 11, 'f': 2},
    'd': {'b': 15, 'c': 11, 'e': 6},
    'e': {'d': 6, 'f': 9},
    'f': {'a': 14, 'c': 2, 'e': 9}
}


class draw_graph:

    def draw_graph_with_matplotlib(self):  # 绘制点之间的邻接关系
        point = list(graph_chain.keys())
        edgelist = []
        for key in graph_chain.keys():
            for v in graph_chain[key].keys():
                edgelist.append((key, v))  # 有重复的
                # print(v)
        print(edgelist)
        G = nx.Graph(edgelist)
        position = nx.circular_layout(G)
        nx.draw_networkx_nodes(G, position, nodelist=point, node_color="r")
        nx.draw_networkx_edges(G, position)
        nx.draw_networkx_labels(G, position)
        labels = {}
        for p in graph_chain.keys():
            for q in graph_chain[p].keys():
                labels[(p, q)] = graph_chain[p][q]
        nx.draw_networkx_edge_labels(G, position, edge_labels=labels)
        plt.show()


if __name__ == '__main__':
    # 绘制图形
    dg = draw_graph()
    dg.draw_graph_with_matplotlib()

    # dijkstra
    # gp = graph(chain=graph_chain)
    # dp = dijkstra_path(gp, 'e')
    # result = dp.find_shortestPath('a')
    # print(result)
