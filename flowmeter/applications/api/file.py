# coding=utf-8

from flowmeter.applications.core import file as core


def generate_file_path():
    return core.generate_tmp_file_path()


def save_file(file, path):
    """
    将二进制文件对象保存在本地磁盘上
    :param path:
    :param file:
    :return:
    """

    core.save_file(file, path)