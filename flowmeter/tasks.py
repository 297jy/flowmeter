# coding=utf-8

import time
from flowmeter.celery import app

from celery.utils.log import get_task_logger
logger = get_task_logger('log')


# this is a function about need many time
@app.task
def add(a, b):
    logger.info('开始执行异步任务！')
    time.sleep(5)
    return a + b

