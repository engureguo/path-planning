import numpy as np

# 无向图
graph_chain = {
    0: {1: 4, 2: 6, 3: 6},
    1: {0: 4, 2: 1, 4: 7},
    2: {0: 6, 1: 1, 4: 6, 5: 4},
    3: {0: 6, 5: 5},
    4: {1: 7, 2: 6, 6: 6},
    5: {2: 4, 3: 5, 4: 1, 6: 8},
    6: {4: 6, 5: 8}
}
point = [0, 1, 2, 3, 4, 5, 6]


class dijkstra_demo:

    def __init__(self, graph, point):
        self.graph = graph  # 邻接链表
        self.point = point  # 所有点集合
        self.path = {}
        self.dist = {}

    def dijkstra_init(self):  # 搜索前初始化 path 和 dist
        for p in self.point:
            self.path[p] = -1  # 所有点都没有父节点，使用-1标记
            self.dist[p] = np.inf  # 到每个点的距离都是无穷大

    def get_shortest_path(self, p):  # p到其他点的最短距离
        if p not in point:
            return []
        self.dijkstra_init()
        unchecked = []  # 未标记的集合
        checked = []  # 最优路径节点
        unchecked.append(p)
        self.path[p] = p
        self.dist[p] = 0
        # 1.每次从未标记的节点中选择距离出发点最近的节点，标记，收录到最优路径集合中
        # 2.计算刚加入节点A的邻接点B的距离，如果 path_P_A + path_A_B < path_P_B 则更新节点B的距离

        while len(unchecked) != 0:
            # 找出 unchecked 中距离距离出发点最近的点
            min_dis = np.inf
            min_point = np.inf
            for k, v in self.dist.items():
                if v < min_dis and k not in checked:
                    min_dis = v
                    min_point = k
            if min_point == np.inf:
                break
            checked.append(min_point)
            unchecked.remove(min_point)
            # 将找到的节点的邻接点加入得到 未标记的集合，同时更新路径
            for k, v in self.graph[min_point].items():
                if k in checked:
                    continue
                if k not in unchecked:  # 还没有标记的点直接加入
                    self.dist[k] = min_dis + v
                    self.path[k] = min_point
                    unchecked.append(k)
                    continue
                if min_dis + v < self.dist[k]:  # 标记过的点，进行路径长度比较
                    self.dist[k] = min_dis + v
                    self.path[k] = min_point

        print(self.dist)
        print(self.path)


d = dijkstra_demo(graph_chain, point)
d.get_shortest_path(0)
