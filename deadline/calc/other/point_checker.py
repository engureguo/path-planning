def is_suggested_point(type1):
    '''
    type是不是建议观测点
    :param type:
    :return:
    '''
    if type1 == 4:
        return True
    return False


def is_path_point(type1):
    '''
    type是不是路径点
    :param type:
    :return:
    '''
    if type1 == 2:
        return False
    return True


def get_spec_point_by_no(p_list, no):
    '''
    根据no，从一个集合中查找一个点
    :param p_list:
    :param no:
    :return:
    '''
    for p in p_list:
        if p['no'] == no:
            return p
    return {}
