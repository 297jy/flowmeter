# coding=utf-8


def get_salt(password):
    """
    获得用于加密的盐
    :parameter password: 获取密码的盐
    :return:
    """

    pass_len = len(password)

    if pass_len == 0:
        return ""

    # 取头、尾、中间的三个字符用于盐字符串的前缀
    head = password[0]
    tail = password[pass_len-1]
    mid = password[int((pass_len - 1) / 2)]

    salt = head + "cqust" + mid + "flowmeter" + tail + "cwq"
    return salt