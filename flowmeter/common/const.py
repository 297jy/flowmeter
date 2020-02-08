# coding=utf-8


class RoleType:
    """
    用户角色基本类型：管理员，厂商，DTU用户。
    这几种基本类型的名称不能够被编辑
    """
    ADMIN = 'admin'
    MANUFACTURER = 'manufacturer'
    DTU_USER = 'dtu_user'


class UserStateType:
    """
    用户状态
    """
    FORBIDDEN_STATE = 'forbidden'
    ENABLE_STATE = 'enable'


DEFAULT_PASSWORD = "111111"
