# coding=utf-8
from flowmeter.config.api import cache
from flowmeter.config.db.configure_table import Configure
from django.db import transaction


def get_unexecuted_opr_check_time():
    """
    获取未执行的操作的检查时间
    例如：每5秒检查是否有操作还未执行
    :return:
    """
    key = 'unexecuted_opr_check_time'
    check_time = cache.get_hash('configure', key)
    # 如果不存在缓存中，则从数据库中读取
    if check_time is None:
        check_time = Configure.objects.get(name=key).val
        check_time = int(check_time)
        cache.set_hash('configure', key, check_time)

    return int(check_time)


def set_unexecuted_opr_check_time(check_time):
    """
    获取未执行的操作的检查时间
    例如：每5秒检查是否有操作还未执行
    :return:
    """
    key = 'unexecuted_opr_check_time'
    conf = Configure.objects.get(name=key)
    conf.val = str(check_time)

    with transaction.atomic():
        conf.save()
        cache.set_hash('configure', key, check_time)