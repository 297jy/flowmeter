# coding=utf-8

import math
import logging

LOG = logging.getLogger('log')


def byte_arr_convert_signed_int(byte_arr):

    num = ""
    for byte in byte_arr:
        num = num + '{:02x}'.format(byte)

    return int(num, 16)


def byte_arr_convert_int(byte_arr):

    res = 0
    for byte in byte_arr:
        res = (res << 8) + byte

    return res


def calculate_double(byte_arr):

    bits = byte_arr[3] & 0xff | (byte_arr[2] & 0xff) << 8 | (byte_arr[1] & 0xff) << 16 | (byte_arr[0] & 0xff) << 24
    sign = 1 if (bits & 0x80000000) == 0 else -1
    exponent = (bits & 0x7f800000) >> 23
    mantissa = bits & 0x007fffff
    mantissa |= 0x00800000
    return sign * mantissa * math.pow(2, exponent - 150)