# coding=utf-8

import json

import logging

from django.db import IntegrityError
from flowmeter.celery import app
from flowmeter.common.const import RoleType
from flowmeter.config.api import user as conf_user_api
from flowmeter.config.api import log as conf_log_api
from flowmeter.config.api import cache as conf_cache_api
from flowmeter.config.api import alarm_log_reader as conf_reader_api
from flowmeter.applications.api import log as app_log_api

logger = logging.getLogger('log')


def send_alarm(alarm_log_dict):
    """
    向用户发送警报
    :return:
    """
    alarm_log = conf_log_api.add_alarm_log(alarm_log_dict)
    # 向管理员推送警报
    admin_ids = conf_user_api.get_all_admin_ids()
    logger.info(admin_ids)
    for admin_id in admin_ids:
        try:
            reader = conf_reader_api.add_unread_alarm({'alarm_log': alarm_log, 'user_id': int(admin_id)})
            alarm_log_dict = {'alarm_reader_id': reader.id, 'msg': app_log_api.render_msg(alarm_log,
                                                                                          RoleType.ADMIN)}
            conf_cache_api.publish_message('alarm_user_id_{}'.format(admin_id), json.dumps(alarm_log_dict))
        except IntegrityError:
            pass
    # 还需要向流量计的厂商推送警报
    man_id = alarm_log.meter.dtu.region.manufacturer.id
    try:
        reader = conf_reader_api.add_unread_alarm({'alarm_log': alarm_log, 'user_id': man_id})
        alarm_log_dict = {'alarm_reader_id': reader.id, 'msg': app_log_api.render_msg(alarm_log,
                                                                                      RoleType.MANUFACTURER)}
        conf_cache_api.publish_message('alarm_user_id_{}'.format(man_id), json.dumps(alarm_log_dict))
    except IntegrityError:
        pass

    # 还需要向DTU用户推送警报
    user_id = alarm_log.meter.dtu.user.id
    try:
        reader = conf_reader_api.add_unread_alarm({'alarm_log': alarm_log, 'user_id': user_id})
        alarm_log_dict = {'alarm_reader_id': reader.id, 'msg': app_log_api.render_msg(alarm_log,
                                                                                      RoleType.DTU_USER)}
        conf_cache_api.publish_message('alarm_user_id_{}'.format(man_id), json.dumps(alarm_log_dict))
    except IntegrityError:
        pass
