# coding=utf-8
"""
每隔10分钟检查一次
"""
import socket


def is_flowmeter_server_running(ip='127.0.0.1', port=8081):
    """流量计服务器是否运行"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, int(port)))
        # 利用shutdown()函数使socket双向数据传输变为单向数据传输。shutdown()需要一个单独的参数，
        # 该参数表示了如何关闭socket。具体为：0表示禁止将来读；1表示禁止将来写；2表示禁止将来读和写。
        s.shutdown(2)
        return True
    except:
        return False
