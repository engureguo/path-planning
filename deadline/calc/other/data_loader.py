import json


def write_dic_to_json(list, file_name):
    '''
    写入json文件
    :param list: 字典列表
    :param file_name: 文件存放路径
    :return:
    '''
    with open(file_name, 'w')as f:
        f.write(json.dumps(list, indent=4))


def load_json_to_dic(file_name):
    '''
    从json文件加载dic对象
    :param file_name:
    :return:
    '''
    with open(file_name, 'r')as f:
        return json.load(f)
