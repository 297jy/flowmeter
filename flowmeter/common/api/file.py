# coding=utf-8

import os


def del_file(filename):

    if os.path.exists(filename):
        os.remove(filename)


def ensure_directory_exist(path):
    """
    确保路径中的文件夹一定存在
    :param path
    :return:
    """
    # 分割路径中的
    directory, file = os.path.split(path)

    if not os.path.exists(directory):
        os.makedirs(directory)