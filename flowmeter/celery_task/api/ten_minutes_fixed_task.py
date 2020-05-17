# coding=utf-8
"""
每隔10分钟检查一次
"""
from flowmeter.init import start_flowmeter_server
from flowmeter.init import init_role_version
from flowmeter.init import init_configure
from flowmeter.celery_task.core import ten_minutes_core
from flowmeter.celery import app


@app.task
def check_system_env():
    """检查系统环境是否正常，不正常则重新初始化"""
    # 没有在运行，就启动服务器
    if not ten_minutes_core.is_flowmeter_server_running():
        start_flowmeter_server()

    # 初始化角色信息
    init_role_version()

    # 初始化系统基本配置参数
    init_configure()
