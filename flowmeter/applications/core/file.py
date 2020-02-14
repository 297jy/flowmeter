# coding=utf-8

import uuid
import os
from flowmeter.settings import BASE_DIR
from flowmeter.common.api import file as file_api


def generate_tmp_file_name(suffix='file'):
    """
    产生一个临时文件名，这个文件夹下的文件，会被定时清理
    :return:
    """
    filename = str(uuid.uuid1()) + '.' + suffix

    return filename


def save_file(file, path):
    """
    将文件保存在磁盘
    :param path: 文件保存路径
    :param file: 文件二进制对象
    :return:
    """

    file_api.ensure_directory_exist(path)

    f = open(path, 'wb')
    for i in file.chunks():
        f.write(i)
    f.close()


def del_file(filename):

    file_api.del_file(filename)


def open_file(filename, mode='rb'):

    file = open(filename, mode)

    return file
