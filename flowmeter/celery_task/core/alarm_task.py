# coding=utf-8

from flowmeter.common.const import RoleType


def render_msg(alarm_log, role_type):

    if role_type == RoleType.ADMIN:
        return "供气商：{}，DTU用户：{}，DTU编号：{}，发生了：{}！".\
            format(alarm_log.meter.dtu.region.manufacturer.name, alarm_log.meter.dtu.user.name,
                   alarm_log.meter.dtu.dtu_no, alarm_log.get_display_alarm_type())
    elif role_type == RoleType.MANUFACTURER:
        return "DTU用户：{}，DTU编号：{}，发生了：{}！". \
            format(alarm_log.meter.dtu.user.name,
                   alarm_log.meter.dtu.dtu_no, alarm_log.get_display_alarm_type())
    elif role_type == RoleType.DTU_USER:
        return "DTU编号：{}，发生了：{}！". \
            format(alarm_log.meter.dtu.dtu_no, alarm_log.get_display_alarm_type())