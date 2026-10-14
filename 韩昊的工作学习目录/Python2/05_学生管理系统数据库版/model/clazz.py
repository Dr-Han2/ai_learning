"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Clazz:
    """班级类"""
    id: int | None = None
    name: str | None = None
    teacher_name: str | None = None
    create_time: datetime | None = None
    update_time: datetime | None = None

    @staticmethod
    def from_dict(dic):
        """从字典到对象"""
        if dic is None:
            return None

        return Clazz(**dic)