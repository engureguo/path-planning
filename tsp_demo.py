# travelling salesman problem

# 贪心算法
# https://www.cnblogs.com/larryking/p/5734459.html
# https://www.bilibili.com/video/av417137546/

import DataProcess as DP  # 加载单源最短路径 shortestpaths.json
import CalShortestPathsForEachPoints as calc_paths
import numpy as np

TOTAL_POINT_NUM = 27  # 0-26


class tsp_solver_demo:

    def __init__(self):
        self.points = DP.load_points()
        self.cal_path_obj = calc_paths.my_calculation()  # 计算单源路径的实例
        self.graph_matrix = {}

    # 判断点的类型
    def get_point_type(self, no):
        for p in self.points:
            if p['no'] == no:
                return p['type']
        return -1

    # 计算必须经过的点即 起点和建议观测点no_int 组成的邻接矩阵，使用 graph_matrix { 0:{"dist":{}, "path":{} }, ,,}
    def get_path_matrix_on_no(self, no_int, dist_dic, path_dic, type_int):
        if type_int == 4 or type_int == 1:
            self.graph_matrix[no_int] = {}
            # self.graph_matrix[no_int]['path'] = path_dic # 路径信息，暂时不用
            self.graph_matrix[no_int]['dist'] = {}
            for p, d in dist_dic.items():
                if int(p) == no_int:
                    self.graph_matrix[no_int]['dist'][p] = -1
                    continue
                p_type = self.get_point_type(int(p))
                if p_type == 1 or p_type == 4:
                    self.graph_matrix[no_int]['dist'][p] = d

    def get_matrix(self):
        # 0 - 26
        self.graph_matrix = {}  # no:{ "path":{}, "dist":{} }
        shortest_path_list = DP.load_json_to_dic('shortestpaths.json')
        for p_info in shortest_path_list:
            self.get_path_matrix_on_no(p_info['no'], p_info['dist'],
                                       p_info['path'], self.get_point_type(p_info['no']))

    def my_tsp_solver(self):
        # 1.使用 CalShortestPathsForEachPoints.py 计算并加载数据
        self.cal_path_obj.calculate_shortest_points()
        # 2.加载数据，计算临界矩阵
        self.get_matrix()
        # print(self.graph_matrix) 查看生成的矩阵
        # 3.使用旅行商算法，根据邻接矩阵计算最短路径
        path = []  # 拟路径, int
        cur_no = start_no = 0
        path.append(cur_no)
        remaining = TOTAL_POINT_NUM  # 27
        while True:
            if remaining == 1:
                path.append(start_no)
                break
            # 从 graph_matrix[cur_no] 中找距离 cur_no 最近的点   a,b,c,d,e --> a b c d e a
            min_dist = np.inf
            min_point = ''
            for p, d in self.graph_matrix[cur_no]['dist'].items():
                p_int = int(p)
                if d != -1 and p_int not in path and d < min_dist:
                    min_dist = d
                    min_point = p_int
            if min_dist != np.inf:
                cur_no = min_point  # 距离 cur_no 最近的未经过的点
                path.append(min_point)
                remaining -= 1
        print('起点为' + str(start_no) + '，经过所有检测点的最短路径是：')
        print(path)


tsp_solver_demo().my_tsp_solver()

# [0, 39, 41, 42, 54, 43, 36, 77, 76, 78, 79, 80, 64, 63, 61, 60, 69, 74, 75, 72, 56, 53, 52, 50, 49, 73, 65, 0]
