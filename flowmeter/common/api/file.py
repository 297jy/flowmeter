# coding=utf-8

import os
import uuid
import zipfile
from flowmeter.settings import TMP_FILE_DIRECTORY_PATH


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


def generate_temp_file_name(suffix=''):
    """
    生成一个临时文件名
    :return:
    """
    filename = os.path.join(TMP_FILE_DIRECTORY_PATH, str(uuid.uuid4()))
    if suffix:
        filename = filename + '.' + suffix
    return filename


def compress_file(file_list):
    """
    压缩文件
    :param file_list: 需要压缩的文件列表
    :return: 并返回文件路径
    """
    path = generate_temp_file_name('zip')
    f = zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED)
    for filepath in file_list:
        f.write(filepath, os.path.split(filepath)[1])
    f.close()
    # 获取文件名
    filename = os.path.split(path)[1]
    return filename
