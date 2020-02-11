# coding=utf-8


class NotFoundActionException(Exception):
    """
        找不到动作相对应的处理器时抛出的异常
    """


class ParameterErrorException(Exception):
    """
        函数参数错误异常
    """


class NotUniqueException(Exception):
    """
        值不唯一异常
    """


class DoesNotExistException(Exception):
    """
        值不存在时，抛出的异常
    """


class ValueValidException(Exception):
    """
    非法值异常
    """


class ForbiddenException(Exception):
    """
    禁止操作异常
    """

