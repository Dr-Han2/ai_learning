"""
@Author  : 韩昊
@Company : 未来元启
@Date    : 2026/10/9 10:18
@Version : 1.0
"""
from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    """登录用户类"""
    id: int |None=None
    username: str | None= None
    password: str  |None=None
    real_name: str | None= None
    create_time: datetime | None= None
    update_time: datetime | None= None

    @staticmethod
    def from_dict(dic):
        """从字典到对象"""
        if dic is None:
            return None
        return User(**dic)