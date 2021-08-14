# 根据 a_star 算出的单元最短路径，使用 TSP算法求出一条最短路径，从开始点到开始点

# 参考 tsp_demo.py 中的实现
# 根据文档，在建议检测点进行检测，而非仪表点(图7黑点)
import other.point_checker as checker
import other.data_loader as loader
import numpy as np


def my_tsp_solver_for_astar():
    points = loader.load_json_to_dic('resources/data.json')
    path_list = loader.load_json_to_dic('resources/paths.json')

    remaining = 27  # 共27个建议监测点
    path0 = []
    cur_no = start_no = 0
    path0.append(cur_no)
    while True:
        if remaining == 1:
            path0.append(start_no)
            break
        cur_p = get_point_info(path_list, cur_no)
        if len(cur_p) == 0:
            break
        min_dist = np.inf
        min_point = -1
        for no_str, info_dic in cur_p['to'].items():
            no_int = int(no_str)
            if no_int not in path0 and checker.is_suggested_point(get_point_type(points, no_int)) \
                    and info_dic['cost'] < min_dist:
                min_dist = info_dic['cost']
                min_point = no_int
        if min_dist == np.inf:
            print('error ---------------------')
            return
        cur_no = min_point
        path0.append(min_point)
        remaining -= 1
    print('起点为' + str(start_no) + '，经过所有检测点的最短路径是：')
    print(path0)
    return path0, points, path_list


def get_point_info(a_list, no):
    for p in a_list:
        if p['no'] == no:
            return p
    return {}


def get_point_type(points, no):
    for p in points:
        if p['no'] == no:
            return p['type']
    return -1


def get_sub_path(no_from, no_to, paths):
    for p in paths:
        if p['no'] == no_from:
            for q, info in p['to'].items():
                if int(q) == no_to:
                    return info['path']
    return []


def get_all_path_point(path0, paths):
    path1 = [0]  # 目标路径
    for i in range(1, len(path0)):
        sub_path = get_sub_path(path0[i - 1], path0[i], paths)
        # print(sub_path)
        if len(sub_path) >= 2:
            for p in sub_path[1:]:
                path1.append(p)
    print("最终的路径：")
    print(path1)


if __name__ == "__main__":
    # 建议观测点，所有点，所有点的最短路径
    path0, points, path_list = my_tsp_solver_for_astar()
    get_all_path_point(path0, path_list)

# 问题：在建议监测点和起点做TSP路径规划
# 尝试，在 建议监测点和起点，以及路径点上做路径规划
