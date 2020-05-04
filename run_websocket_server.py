# coding=utf-8
"""websocket服务器运行脚本"""
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flowmeter.settings')
django.setup()

from flowmeter.websocket.api import server

if __name__ == "__main__":

    server.server_socket()