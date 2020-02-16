# coding=utf-8

from flowmeter.celery import app


@app.task
def update_opr_result(dtu_no, frame):

    pass