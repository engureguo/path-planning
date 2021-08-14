# A*算法，已知一个无向有权图，根据某种代价计算方法，可求得 start 到 end 的最短路径


A = 0  # Arad
B = 1  # Bucharest
C = 2  # Craiova
D = 3  # Dobreta
E = 4  # Eforie
F = 5  # Fagaras
G = 6  # Giurgiu
H = 7  # Hirsova
I = 8  # Iasi
L = 9  # Lugoj
M = 10  # Mehadia
N = 11  # Neamt
O = 12  # Oradea
P = 13  # Pitesti
R = 14  # Rimnicu Vilcea
S = 15  # Sibiu
T = 16  # Timisoara
U = 17  # Urziceni
V = 18  # Vaslui
Z = 19  # Zerind

# 构建一个20*20的矩阵
PLACES_NUM = 20


# 地图
class Graph:
    def __init__(self):
        self.romania_graph = [[0] * PLACES_NUM for i in range(PLACES_NUM)]

    def add_edge(self, _from, _to, _value):
        if _from < PLACES_NUM:
            if _to < PLACES_NUM:
                # 无向图 = 双向有向图
                self.romania_graph[_from][_to] = _value
                self.romania_graph[_to][_from] = _value

    def get_edge(self, _from, _to):
        return self.romania_graph[_from][_to]


# 问题的最终解
class Stack:

    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)
        return

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        if self.stack:
            return False
        return True


# CLOSED表
class Queue:
    def __init__(self):
        self.queue = []  # close 表中记录已访问过的节点

    def put(self, value):
        self.queue.append(value)
        return

    def get(self):
        return self.queue.pop(0)

    def contain(self, value):
        return value in self.queue

    def is_empty(self):
        if self.queue:
            return False
        return True


# OPEN表，拟优先级队列，从小到大排序，get() 获取到 cost 最小值对应的点
class PriorityQueue:

    def __init__(self):
        self.queue = []  # open表，保存已生成而未检测的节点

    def put(self, node_cost):
        """
        :param node_cost: [value,cost]
        """
        self.queue.append(node_cost)  # [ [p_no, p_cost], [], [] ]

    def get(self):
        if self.queue:
            min_i = 0
            min_cost = self.queue[min_i][1]
            for i in range(len(self.queue)):
                if self.queue[i][1] < min_cost:  # queue[x][1] 表示代价
                    min_i = i
                    min_cost = self.queue[i][1]
            return self.queue.pop(min_i)

    def contain(self, value):
        for i in range(len(self.queue)):
            if self.queue[i][0] == value:  # queue[x][0] 表示坐标
                return self.queue[i], True
        return None, False

    def is_empty(self):
        if self.queue:
            return False
        return True

    def remove_val_and_cost(self, value):
        for i in range(len(self.queue)):
            if self.queue[i][0] == value:
                self.queue.pop(i)
                return


# initialize undirected graph
# 初始化无向图
def init_graph():
    graph = Graph()

    graph.add_edge(O, Z, 71)
    graph.add_edge(O, S, 151)
    graph.add_edge(A, Z, 75)
    graph.add_edge(A, S, 140)
    graph.add_edge(A, T, 118)
    graph.add_edge(T, L, 111)
    graph.add_edge(L, M, 70)
    graph.add_edge(M, D, 75)
    graph.add_edge(D, C, 120)
    graph.add_edge(S, R, 80)
    graph.add_edge(S, F, 99)
    graph.add_edge(R, C, 146)
    graph.add_edge(F, B, 211)
    graph.add_edge(R, P, 97)
    graph.add_edge(C, P, 138)
    graph.add_edge(P, B, 101)
    graph.add_edge(B, G, 90)
    graph.add_edge(B, U, 85)
    graph.add_edge(U, H, 98)
    graph.add_edge(U, V, 142)
    graph.add_edge(V, I, 92)
    graph.add_edge(I, N, 87)
    graph.add_edge(H, E, 86)

    return graph


# graph 二维数组，无向图，gra[i][j] = weight
# h 一维数组，对应索引，关于该节点的一个值
# _root 起点，索引
# _goal 重点，索引
def a_star(graph, h, _root, _goal):
    parents = [-1] * PLACES_NUM  # temporary parents             现阶段搜索过程中的每个节点的父结点记录@
    pq_open = PriorityQueue()  # open queue                     初始化open表@
    q_close = Queue()  # closed queue                           初始化closed表@
    pq_open.put([_root, 0])  # 将初始结点存入OPEN表中@

    while not pq_open.is_empty():
        parent_node = pq_open.get()  # 获取cost最小点
        q_close.put(parent_node[0])  # 将open表中的cost最小的节点放入close表
        if parent_node[0] == _goal:  # cost最小的节点是否是目标节点
            break
        for i in range(20):  # 拓展cost最小的节点
            length = graph.get_edge(parent_node[0], i)
            if length != 0:  # 边 (i, parent_node[0]) 存在
                node, result = pq_open.contain(i)  # 查看open表中知否已经存在该节点

                # 计算代价？？？
                f = parent_node[1] + length + h[i] - h[parent_node[0]]  # 计算 cost

                if q_close.contain(i):  # 节点 i 已经在 close表中
                    continue
                elif result:  # 节点 i 在open表中，需要重新估算节点
                    if node[1] > f:  #
                        pq_open.remove_val_and_cost(node[0])  # 完整删除
                        parents[i] = parent_node[0]  # i节点来自cost最小点即parent_node[0]
                        pq_open.put([i, f])
                else:  # 节点i不在open表中，则需要加入
                    parents[i] = parent_node[0]  # i节点来自cost最小点即parent_node[0]
                    pq_open.put([i, f])
    path = []
    cost = 0
    print("parents:")
    for i in range(len(parents)):
        print(str(i) + '(' + chr(i + 65) + ')' + ' 的父节点是 ' + str(parents[i]))

    print('---------------------')
    p = _goal
    while p != _root:
        cost += graph.get_edge(p, parents[p])
        path.append(p)
        p = parents[p]

    length = len(path) - 1
    print('path:', _root, end='')
    for i in range(length + 1):
        print(" -->", path[length - i], end='')
    print()
    return cost


if __name__ == '__main__':
    graph = init_graph()


    # 每个结点的代价
    # h = (366, 0, 160, 242, 161,
    #      178, 77, 151, 226, 244,
    #      241, 234, 380, 98, 193,
    #      253, 329, 80, 199, 374)
    h = [0 for i in range(20)]

    start_point = 'U'
    end_point = 'A'
    print(start_point, 'to', end_point)
    cost = a_star(graph, h, eval(start_point), eval(end_point))
    print('cost:', cost)
