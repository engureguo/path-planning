import json
import math


# 结合原始点文件 data.json，计算原始边的权值，写入edges2.json

class DistanceCalculator:

    def __init__(self, edges, points):
        self.edges = edges
        self.points = points

    @staticmethod
    def get_distance(p1, p2):  # 两点之间的距离
        dx = p1[0] - p2[0]
        dy = p1[1] - p2[1]
        ds = math.sqrt((math.pow(dx, 2) + math.pow(dy, 2)))
        return ds

    def get_point_info(self, no):
        for p in self.points:  # O-N，慢
            if p['no'] == no:
                return p
        return {}

    def is_path_point(self, no):  # 是否为路径点（路径点可达，区别于仪表点不可达），通过type判断
        p_dic = self.get_point_info(no)
        if p_dic['type'] != 2:
            return True
        return False

    def get_all_weight(self):
        new_list = []
        for e in self.edges:
            if self.is_path_point(e['p']) and self.is_path_point(e['q']):
                p = self.get_point_info(e['p'])
                q = self.get_point_info(e['q'])
                w = self.get_distance((p['x'], p['y']), (q['x'], q['y']))
                e2 = e.copy()  # 浅拷贝
                e2['w'] = round(w, 3)  # 权值
                new_list.append(e2)
            else:
                e2 = e.copy()
                e2['valid'] = False
        with open('edges2.json', 'w')as f:
            f.write(json.dumps(new_list, indent=4))


# d = R
# dc = DistanceCalculator(d.load_edges(), d.load_points())
# dc.get_all_weight()  # 计算边的权值，写入 edges2.json 中
