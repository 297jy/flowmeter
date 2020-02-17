# coding=utf-8
import re
import validators
from voluptuous import Schema
from voluptuous import MultipleInvalid
from voluptuous import Required
from flowmeter.exceptions import ParameterErrorException
from flowmeter.common.const import RoleType
from flowmeter.common.const import UserStateType
from flowmeter.config import const
from flowmeter.config.db.operator_table import Operator
from flowmeter.config.db.log_table import AlarmLog, OprLog


def param_check(data, must_dict=None, optional_dict=None, extra=False):

    """
    api参数校验函数
    :param data: dict，被校验的数据
    :param must_dict: dict, 必要参数字典
    :param optional_dict: dict，可选参数字典
    :param extra: bool, 是否能存在额外的参数
    :return: 校验失败就抛异常
    """
    if not isinstance(data, dict):
        raise ParameterErrorException("data参数：{}，不是字典！".format(data))

    schema_dict = {}
    if must_dict:
        for key, val in must_dict.items():
            schema_dict[Required(key)] = val
    if optional_dict:
        for key, val in optional_dict.items():
            schema_dict[key] = val

    schema = Schema(schema_dict, extra=extra)
    try:
        schema(data)
    except MultipleInvalid as e:
        raise ParameterErrorException("参数校验失败，{}！".format(e.errors))


class StrCheck:
    @staticmethod
    def check_is_str(string):
        if not isinstance(string, str):
            raise ParameterErrorException("string的值：{}，不是字符串类型！".format(string))

    @staticmethod
    def check_not_null(string):

        StrCheck.check_is_str(string)

        if not string:
            raise ParameterErrorException("string的值：{}为空值".format(string))

    @staticmethod
    def check_admin_name(admin_name):

        StrCheck.check_not_null(admin_name)

        if len(admin_name) > const.NAME_CHAR_LEN:
            raise ParameterErrorException("管理员名称长度只能为[1-{}]个字符！".format(const.NAME_CHAR_LEN))

        if not re.match(r'[\u4e00-\u9fa5a-zA-Z0-9]+$', admin_name):
            raise ParameterErrorException("管理员名称只能为中文、大小写字母、数字！")

    @staticmethod
    def check_email(email):

        if not validators.email(email):
            raise ParameterErrorException("{}，不是合法的邮箱格式！".format(email))

    @staticmethod
    def check_phone(phone):

        StrCheck.check_not_null(phone)

        if not re.match(r'[0-9]{11}$', phone):
            raise ParameterErrorException("{}，不是合法的电话格式！".format(phone))

    @staticmethod
    def check_remark(remark):

        StrCheck.check_is_str(remark)

        if len(remark) > const.REMARK_CHAR_LEN:
            raise ParameterErrorException("备注字符长度只能为[0-{}]个字符！".format(const.REMARK_CHAR_LEN))

    @staticmethod
    def check_password(password):

        StrCheck.check_not_null(password)

        if len(password) > const.PASSWORD_CHAR_LEN:
            raise ParameterErrorException("密码字符长度只能为[1-{}]个字符！".format(const.PASSWORD_CHAR_LEN))

    @staticmethod
    def check_navigation_bar_name(name):

        StrCheck.check_not_null(name)

        if len(name) > const.NAVIGATION_BAR_NAME_CHAR_LEN:
            raise ParameterErrorException("导航栏名称字符长度只能为[1-{}]个字符！"
                                          .format(const.NAVIGATION_BAR_NAME_CHAR_LEN))

    @staticmethod
    def check_navigation_bar_icon(icon):

        StrCheck.check_not_null(icon)

        if len(icon) > const.NAVIGATION_BAR_ICON_CHAR_LEN:
            raise ParameterErrorException("导航栏图标字符长度只能为[1-{}]个字符！"
                                          .format(const.NAVIGATION_BAR_ICON_CHAR_LEN))

    @staticmethod
    def check_auth_category_name(name):

        StrCheck.check_not_null(name)

        if len(name) > const.AUTH_CATEGORY_NAME_CHAR_LEN:
            raise ParameterErrorException("导航栏名称字符长度只能为[1-{}]个字符！"
                                          .format(const.AUTH_CATEGORY_NAME_CHAR_LEN))

    @staticmethod
    def check_auth_name(name):

        StrCheck.check_not_null(name)

        if len(name) > const.AUTH_NAME_CHAR_LEN:
            raise ParameterErrorException("权限名称字符长度只能为[1-{}]个字符！"
                                          .format(const.AUTH_NAME_CHAR_LEN))

    @staticmethod
    def check_auth_permission_action(action):

        StrCheck.check_not_null(action)

        if len(action) > const.AUTH_PERMISSION_ACTION_CHAR_LEN:
            raise ParameterErrorException("权限行为名称字符长度只能为[1-{}]个字符！"
                                          .format(const.AUTH_PERMISSION_ACTION_CHAR_LEN))

    @staticmethod
    def check_url(url):

        StrCheck.check_not_null(url)

        if len(url) > const.URL_CHAR_LEN:
            raise ParameterErrorException("URL字符长度只能为[1-{}]个字符！"
                                          .format(const.URL_CHAR_LEN))


class WhiteListCheck:

    @staticmethod
    def check_role_type(role_type):
        role_type_list = [RoleType.ADMIN, RoleType.MANUFACTURER, RoleType.DTU_USER]

        for now_role in role_type_list:
            if now_role == role_type:
                return

        raise ParameterErrorException("{} 不属于系统的基本角色：{}", format(role_type, str(role_type_list)))

    @staticmethod
    def check_user_state_type(state_type):

        state_type_list = [UserStateType.ENABLE_STATE, UserStateType.FORBIDDEN_STATE]

        for now_state in state_type_list:
            if now_state == state_type:
                return

        raise ParameterErrorException("{} 不属于用户状态的基本类型：{}", format(state_type, str(state_type_list)))

    @staticmethod
    def check_opr_type(opr_type):

        type_list = [
            Operator.QUERY,
            Operator.RECHARGE,
            Operator.RESET,
            Operator.SET_METER_ADDRESS,
            Operator.CLOSE_VALVE,
            Operator.OPEN_VALVE,
            Operator.CLOSE_RECHARGE,
            Operator.OPEN_RECHARGE,
            Operator.SET_FLOW_RATIO,
        ]

        if opr_type not in type_list:
            raise ParameterErrorException("没有该操作类型：{}！", opr_type)

    @staticmethod
    def check_opr_state(state):

        state_list = [
            OprLog.SUCCESS_STATE,
            OprLog.ERROR_STATE,
            OprLog.WAITE_STATE,
        ]

        if state not in state_list:
            raise ParameterErrorException("没有该操作状态：{}！", state)

    @staticmethod
    def check_alarm_type(alarm_type):

        type_list = [AlarmLog.ALARM_EXCEED_LIMIT, AlarmLog.ALARM_SUB_VALVE, AlarmLog.ALARM_INTERRUPT]
        if alarm_type not in type_list:
            raise ParameterErrorException("没有该警报类型：{}！", alarm_type)

class IntCheck:

    @staticmethod
    def check_is_int(data):
        if not isinstance(data, int):
            raise ParameterErrorException("{} 不是整形值".format(data))


class ListCheck:

    @staticmethod
    def check_is_list(datas):
        if not isinstance(datas, list):
            raise ParameterErrorException("{} 不是列表".format(str(datas)))

    @staticmethod
    def check_is_int_list(datas):
        ListCheck.check_is_list(datas)
        for data in datas:
            IntCheck.check_is_int(data)






