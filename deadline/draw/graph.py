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
        # 20 * 20 邻接矩阵
        self.romania_graph = [[0] * PLACES_NUM for i in range(PLACES_NUM)]

    def __str__(self):
        return str(self.romania_graph)

    def add_edge(self, _from, _to, _value):
        if _from < PLACES_NUM:
            if _to < PLACES_NUM:
                self.romania_graph[_from][_to] = _value
                self.romania_graph[_to][_from] = _value

    def get_edge(self, _from, _to):
        return self.romania_graph[_from][_to]

    def get(self):
        return self.romania_graph


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


# if __name__ == '__main__':
#     graph = init_graph()
#
#     print(graph)
#
#     # 怎么才能够获取到这个矩阵
#     h = (366, 0, 160, 242, 161,
#          178, 77, 151, 226, 244,
#          241, 234, 380, 98, 193,
#          253, 329, 80, 199, 374)
