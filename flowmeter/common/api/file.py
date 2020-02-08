# coding=utf-8

import os


def del_file(filename):

    if os.path.exists(filename):
        os.remove(filename)
