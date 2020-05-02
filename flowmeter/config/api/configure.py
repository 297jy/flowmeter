# coding=utf-8
from flowmeter.config.api import cache
from flowmeter.config.db.configure_table import Configure
from flowmeter.common.api.validators import StrCheck, param_check
from django.db import transaction


def get_websocket_port_name():
    """获取websocket端口配置名"""
    return "websocket_port"


def get_flowmeter_port_name():
    """获取流量器远程服务器端口配置名"""
    return "flowmeter_port"


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


def get_query_meter_time():
    """
    获取未执行的操作的检查时间
    例如：每5秒检查是否有操作还未执行
    :return:
    """
    key = 'query_meter_time'
    check_time = cache.get_hash('configure', key)
    # 如果不存在缓存中，则从数据库中读取
    if check_time is None:
        check_time = Configure.objects.get(name=key).val
        check_time = int(check_time)
        cache.set_hash('configure', key, check_time)

    return int(check_time)


def set_query_meter_time(check_time):
    """
    获取定时查询流量计的时间间隔
    :return:
    """
    key = 'query_meter_time'
    conf = Configure.objects.get(name=key)
    conf.val = str(check_time)

    with transaction.atomic():
        conf.save()
        cache.set_hash('configure', key, check_time)


def get_all_configure():
    """
    获取所有配置信息
    :return:
    """
    confs = Configure.objects.all()
    return confs


def get_configure_by_name(name):
    """根据配置名获取配置值"""
    val = cache.get_hash('configure', name)
    if val is None:
        val = Configure.objects.get(name=name).val
        cache.set_hash('configure', name, val)
    return val


def update_configure(conf_info):

    must_dict = {
        "name": str,
        "val": StrCheck.check_value,
    }
    param_check(conf_info, must_dict)

    conf = Configure.objects.get(name=conf_info['name'])
    conf.val = conf_info['val']

    with transaction.atomic():
        conf.save()
        # 更新缓存
        cache.set_hash('configure', conf_info['name'], conf_info['val'])