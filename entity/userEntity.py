"""
用户实体类
"""


class User:
    id = None  # 编号
    userName = None  # 用户名
    password = None  # 密码

    def __init__(self, userName, password):
        self.userName = userName
        self.password = password
