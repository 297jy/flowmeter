# coding=utf-8

import time
from flowmeter.celery import app


# this is a function about need many time
@app.task
def add(a, b):
    time.sleep(5)
    return a + b


@app.task
def update_opr_result(dtu_no, frame):

    pass

