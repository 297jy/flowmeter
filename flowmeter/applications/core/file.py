# coding=utf-8

import uuid
import os
from flowmeter.settings import BASE_DIR
from flowmeter.common.api import file as file_api


def generate_tmp_file_path():
    """
    产生一个临时文件名，这个文件夹下的文件，会被定时清理
    :return:
    """
    path = os.path.join(BASE_DIR, 'file', 'tmp', str(uuid.uuid1()) + '.file')
    return path


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