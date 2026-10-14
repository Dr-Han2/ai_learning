"""
@Author  : 韩昊
@Company : 未来元启
@Date    : 2026/10/9 10:17
@Version : 1.0
"""
from dataclasses import dataclass
from datetime import datetime


@dataclass()
class Clazz:
    """班级类"""
    id: int | None = None
    name: str | None = None
    teacher_name: str | None = None
    create_time: datetime | None = None
    update_time: datetime | None = None

    @staticmethod
    def from_dict(dic):
        if dic is None:
            return None
        return Clazz(**dic)