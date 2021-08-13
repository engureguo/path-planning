import numpy as np

# dijkstra算法学习，求图（无向图或有向图）中某一点到其他点的最短路径单源最短路径（单源最短路径）
# 好看视频 https://haokan.baidu.com/v?pd=wisenatural&vid=1146937591908032169

# 无向图（类邻接表，需要双向记录！）
graph_chain = {
    0: {1: 4, 2: 6, 3: 6},
    1: {0: 4, 2: 1, 4: 7},
    2: {0: 6, 1: 1, 4: 6, 5: 4},
    3: {0: 6, 5: 5},
    4: {1: 7, 2: 6, 5: 1, 6: 6},
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
        self.path = {}
        self.dist = {}
        for p in self.point:
            self.path[p] = -1  # 所有点都没有父节点，使用-1标记
            self.dist[p] = np.inf  # 到每个点的距离都是无穷大

    def get_shortest_path(self, p):  # p到其他点的最短距离
        if p not in self.point:
            return {}
        self.dijkstra_init()
        unchecked = []  # 未标记的集合
        checked = []  # 最优路径节点
        unchecked.append(p)
        self.path[p] = p
        self.dist[p] = 0

        while len(unchecked) != 0:
            # 找出 unchecked 中距离距离出发点最近的点
            min_dis = np.inf
            min_point = np.inf
            for k, v in self.dist.items():
                if v < min_dis and k not in checked:
                    min_dis = v
                    min_point = k
            if min_point == np.inf:  # 从未标记的点中没找到离出发点最近的点
                break
            checked.append(min_point)
            unchecked.remove(min_point)
            # 将找到的节点的邻接点加入得到 未标记的集合，同时更新路径
            for k, v in self.graph[min_point].items():

                if k in checked:
                    continue

                if min_dis + v < self.dist[k]:
                    self.dist[k] = round(min_dis + v, 3)
                    self.path[k] = min_point
                    if k not in unchecked:
                        unchecked.append(k)

        # print(self.dist)
        # print(self.path)
        return {"path": self.path, "dist": self.dist}

# d = dijkstra_demo(graph_chain, point)
# print(d.get_shortest_path(0))
