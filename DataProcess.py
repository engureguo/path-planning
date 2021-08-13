import json


# 加载json数据，按照文件名
def load_json_to_dic(file_name):
    with open(file_name, 'r')as f:
        return json.load(f)


# 加载原始边文件
def load_edges():
    with open('edges.json', 'r')as f:
        return json.load(f)


# 加载原始点文件
def load_points():
    # 加载json数据
    with open('data.json', 'r')as f:
        return json.load(f)


# 将原始点写入csv
def write_edges():
    data = load_edges()
    with open('edges.csv', 'w')as f:
        f.write('顶点1,顶点2')
        for row in data:
            f.write('\n' + str(row['p']) + ',' + str(row['q']))


# 将原始点写入csv
def write_points():
    data = load_points()
    # 将json写入csv检查
    with open('data.csv', 'w')as f:
        f.write('编号,x坐标,y坐标,类型id(1起点2仪表点3道路4建议检测点)')
        for row in data:  # row为字典类型
            f.write('\n')
            f.write(str(row['no']) + ',' + str(row['x']) + ',' + str(row['y']) + ',' + str(row['type']))


def write_dic_to_json(list, file_name):
    with open(file_name, 'w')as f:
        f.write(json.dumps(list, indent=4))
