# coding=utf-8

from flowmeter.applications.core import file as core


def generate_file_name():

    return core.generate_tmp_file_name()


def generate_excel_file_name():
    """
    产生一个EXCEL表格
    :return:
    """
    return core.generate_tmp_file_name(suffix='xlsx')


def save_file(file, path):
    """
    将二进制文件对象保存在本地磁盘上
    :param path:
    :param file:
    :return:
    """

    core.save_file(file, path)


def del_file(filename):

    core.del_file(filename)


def read_text_file(filename):
    """
    读取文本文件
    :param filename:
    :return:
    """
    return core.open_file(filename, mode='rt')


def read_binary_file(filename):
    """
    读取二进制文件
    :param filename:
    :return:
    """
    return core.open_file(filename)
