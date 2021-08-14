# 使用 A*算法算出每个点到其他点的最短距离，存入 dist.json 中
# A*算法，已知一个无向有权图，根据某种代价计算方法，可求得 start 到 end 的最短路径

import other.data_loader as loader
import other.point_checker as checker

# 构建矩阵，0-81，路径点为 0，27-80，需要计算路径点 x 到其他路径点的距离
PLACES_NUM = 81


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

    def __str__(self):
        return str(self.romania_graph)

    def get_graph(self):
        return self.romania_graph


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


def init_graph():
    '''
    初始化无向图，加载先前算好的数据（边、权值）
    :return:
    '''
    graph = Graph()
    edges2 = loader.load_json_to_dic('resources/edges2.json')
    for e in edges2:
        graph.add_edge(e['p'], e['q'], e['w'])
    return graph


def a_star(graph, h, _root, _goal):
    '''
    a*算法
    :param graph: 二维数组，无向图，gra[i][j] = weight
    :param h: 一维数组，对应索引，关于该节点的一个值
    :param _root: 起点，索引
    :param _goal: 终点，索引
    :return:
    '''
    parents = [-1] * PLACES_NUM  # temporary parents             现阶段搜索过程中的每个节点的父结点记录@
    pq_open = PriorityQueue()  # open queue                     初始化open表@
    q_close = Queue()  # closed queue                           初始化closed表@
    pq_open.put([_root, 0])  # 将初始结点存入OPEN表中@

    while not pq_open.is_empty():
        parent_node = pq_open.get()  # 获取cost最小点
        q_close.put(parent_node[0])  # 将open表中的cost最小的节点放入close表
        if parent_node[0] == _goal:  # cost最小的节点是否是目标节点
            break
        for i in range(PLACES_NUM):  # 拓展cost最小的节点
            length = graph.get_edge(parent_node[0], i)
            if length != 0:  # 边 (i, parent_node[0]) 存在
                node, result = pq_open.contain(i)  # 查看open表中知否已经存在该节点
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
    cost = 0
    path = []
    # 根据parents数据计算 _root 到 _goal 的路径
    p = _goal
    while p != _root:
        cost += graph.get_edge(p, parents[p])
        # path.append(p)
        path.insert(0, p)
        p = parents[p]  # 从 _goal 找到 _root
    path.insert(0, _root)

    return cost, path


def all_astar_for_all_path_points():
    graph = init_graph()
    h = [0 for i in range(PLACES_NUM)]
    points = loader.load_json_to_dic('resources/data.json')
    new_list = []  # 存放 a* 算法计算出的路径点之间的最短路径及路径长度
    for start in range(PLACES_NUM):
        a_dic = {'no': start, 'type': checker.get_spec_point_by_no(points, start)['type']}
        to_dic = {}
        for end in range(PLACES_NUM):
            if start == end:
                continue
            p = checker.get_spec_point_by_no(points, start)
            q = checker.get_spec_point_by_no(points, end)
            if checker.is_path_point(p['type']) and checker.is_path_point(q['type']):  # 都是路径点
                cost, path = a_star(graph, h, start, end)
                to_spec_dic = {'cost': round(cost, 3), 'path': path}
                to_dic[end] = to_spec_dic
        a_dic['to'] = to_dic
        new_list.append(a_dic)
    return new_list


if __name__ == '__main__':
    get_list = all_astar_for_all_path_points()
    loader.write_dic_to_json(get_list, 'resources/paths.json')  # 写json文件
