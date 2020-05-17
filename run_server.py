# coding=utf-8
"""远程服务器运行脚本"""
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flowmeter.settings')
django.setup()

from flowmeter.modbus.api import server


if __name__ == "__main__":

    server.run_server()