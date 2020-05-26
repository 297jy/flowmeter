from flowmeter.celery import app
from flowmeter.celery_task.api import twelve_fixed_task


@app.task(ignore_result=True)
def statistic_meter_data():
    """
    统计仪表数据，用于生成报表信息
    :return:
    """
    # twelve_fixed_task.statistic_meter_data()
    pass


@app.task(ignore_result=True)
def clean_junk_file():
    # twelve_fixed_task.clean_junk_file()
    pass