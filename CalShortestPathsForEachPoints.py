# 为所有路径点计算到其他路径点的最短距离

import numpy as np
import DataProcess as DP
import learnDijkstra.demo as dijdemo
import DistanceUtil as DU

# 1.计算无向图的邻接表（根据 edges2.json 和 points）
# 2.以路径点为起点进行迭代，计算它们的单源最短路径，结构是 [0: {"path":{}, "dist":{}}, , ,]
#       其中的no：0,27-80，共55个点

MIN_NUM = 0  # 最小编号
MAX_NUM = 80  # 最大编号


class my_calculation:

    def __init__(self, e_file='edges2.json', p_file='data.json'):
        self.points = DP.load_json_to_dic(p_file)
        self.cal_and_write_edges2()  # 使用 DistanceUtil 计算出边的权值，存入 edges2.json
        self.edges2 = DP.load_json_to_dic(e_file)

    @staticmethod
    def cal_and_write_edges2():
        data_calc = DU.DistanceCalculator(DP.load_edges(), DP.load_points())
        data_calc.get_all_weight()
        print('写入 edges2.json 完毕')

    # 根据 points和edges2 计算邻接表
    def get_graph_chain(self):
        my_graph_chain = {}
        for i in range(MIN_NUM, MAX_NUM + 1):
            my_graph_chain[i] = {}
        for e in self.edges2:
            my_graph_chain[e['p']][e['q']] = e['w']
            my_graph_chain[e['q']][e['p']] = e['w']
        return my_graph_chain

    def calculate_shortest_points(self):
        points_list = []
        my_graph_chain = self.get_graph_chain()
        dij = dijdemo.dijkstra_demo(my_graph_chain, [no for no in range(MIN_NUM, MAX_NUM + 1)])
        for p in self.points:
            if p['type'] != 2:  # 非仪表点，是路径点，计算单源最短路径，p['no'] 为起点
                ret_dic = dij.get_shortest_path(p['no'])
                if len(ret_dic) == 0:
                    continue
                # 将结果记录到list中
                points_list.append({"no": p['no'], "path": ret_dic["path"], "dist": self.filter_data(ret_dic["dist"])})
        DP.write_dic_to_json(points_list, "shortestpaths.json")
        print('calculation done!')

    @staticmethod
    def filter_data(dist_dict):
        for k, v in dist_dict.items():
            if v == np.inf:
                dist_dict[k] = -1  # -1代表不可达
        return dist_dict


obj = my_calculation()
obj.calculate_shortest_points()
