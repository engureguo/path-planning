import json


class DataResolve:

    def __init__(self):
        self.data = []

    # 将边写入csv
    def load_edges(self):
        with open('edges.json', 'r')as f:
            self.data = json.load(f)
        return self.data

    def write_edges(self):
        with open('edges.csv', 'w')as f:
            f.write('顶点1,顶点2')
            for row in self.data:
                f.write('\n' + str(row['p']) + ',' + str(row['q']))

    def load_points(self):
        # 加载json数据
        with open('data.json', 'r')as f:
            self.data = json.load(f)
        return self.data

    def write_points(self):
        # 将json写入csv检查
        with open('data.csv', 'w')as f:
            f.write('编号,x坐标,y坐标,类型id(1起点2仪表点3道路4建议检测点)')
            for row in self.data:  # row为字典类型
                f.write('\n')
                f.write(str(row['no']) + ',' + str(row['x']) + ',' + str(row['y']) + ',' + str(row['type']))
