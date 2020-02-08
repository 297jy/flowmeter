# coding=utf-8

from flowmeter.exceptions import NotFoundActionException
from flowmeter.common.api import request as request_api


class Result:

    def __init__(self, success, data=None, msg=''):
        self.success = success
        self.data = data
        self.msg = msg

    @staticmethod
    def success(data, msg='登录成功！'):
        return Result(success=True, data=data, msg=msg)

    @staticmethod
    def error(msg=''):
        return Result(success=False, msg=msg)

    # 获取字典的键
    def keys(self):
        s = ('success', 'msg', 'data')
        return s

    # 获取键对应的值
    def __getitem__(self, item):

        return getattr(self, item)


class ActionHandlerBase:
    """
        动作处理器基类
    """

    def __init__(self, action_dict):
        # 动作字典
        self.action_dict = action_dict

    def get_action_handler(self, request):
        """
        获取动作对应的处理函数
        :param request:
        :return:
        """

        action = request_api.get_action(request)
        handler = self.action_dict.get(action)
        return handler

    def handle(self, request):
        """
        调用动作处理器来处理动作，并返回处理器的执行结果
        :param request:
        :return:
        """
        handler = self.get_action_handler(request)
        if handler:
            return handler(request)
        else:
            raise NotFoundActionException()
