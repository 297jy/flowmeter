# coding=utf-8

import json
import threading

from flowmeter.config.api import role as conf_role_api
from flowmeter.config.api import flag as conf_flag_api
from flowmeter.config.api import cache as conf_cache_api
from flowmeter.config.db.flag_table import Flag
from flowmeter.config.db.configure_table import Configure

from flowmeter.modbus.api import server


ACTION_TYPE_INDEX = 0
MSG_INDEX = 1
DATA_FIELD_INDEX = 2


def init_role_version():
    """
    初始化角色权限版本
    :return:
    """
    roles = conf_role_api.get_all_role()
    for role in roles:
        try:
            conf_flag_api.get_role_version(role.name)
        except Flag.DoesNotExist:
            Flag.objects.create(**{"name": "{}_version".format(role.name), "val": str(1)})


def init_configure():
    """
    初始化系统配置
    :return:
    """
    conf_list = [{
        'label': '检查未执行操作时间间隔（秒）',
        'name': 'unexecuted_opr_check_time',
        'val': 5,
    }, {
        'label': '定时查询流量计时间间隔（分）',
        'name': 'query_meter_time',
        'val': 30,
    }, {
        'label': '登录过期时间',
        'name': 'session_expire_time',
        'val': '关闭浏览器过期',
    }]

    for conf in conf_list:
        try:
            c = Configure.objects.get(name=conf['name'])
            conf_cache_api.set_hash('configure', conf['name'], c.val)
        except Configure.DoesNotExist:
            Configure.objects.create(**conf)
            conf_cache_api.set_hash('configure', conf['name'], conf['val'])


def load_log_configure():
    """
    加载配置文件信息到缓存中
    :return:
    """

    log_conf_file = open('configure/system_log.conf', 'rt', encoding='utf-8')
    while True:
        # 读取配置文件每一行的配置信息
        log_conf_str = log_conf_file.readline()
        if not log_conf_str:
            break
        log_confs = log_conf_str.split('=')

        action_type = log_confs[ACTION_TYPE_INDEX]
        conf_dict = {'msg': log_confs[MSG_INDEX]}
        if DATA_FIELD_INDEX < len(log_confs):
            conf_dict['data_field'] = log_confs[DATA_FIELD_INDEX].strip().split(';')
        else:
            conf_dict['data_field'] = []

        conf_cache_api.set_hash('log_configure', action_type,
                                json.dumps(conf_dict))

    log_conf_file.close()


def start_flowmeter_server():
    """
    开始流量计远程服务器
    :return:
    """
    t = threading.Thread(target=server.run_server, args=())
    t.start()


def main():
    pass


if __name__ == '__main__':
    main()