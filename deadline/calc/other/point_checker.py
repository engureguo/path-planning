def is_path_point(type):
    '''
    type是不是路径点
    :param type:
    :return:
    '''
    if type == 2:
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
