"""
@Author  : hanhao
@Company : 未来元启
@Date    : 2026/10/9 10:18
@Desc    : 
@Version : 1.0
"""
from dataclasses import dataclass
from datetime import datetime



@dataclass
class Student:
    """学生类"""
    id: int | None = None
    stu_num: str | None = None
    name: str | None = None
    gender: str | None = None
    age: int | None = None
    class_id: int | None = None
    phone: str | None = None
    create_time: datetime | None = None
    update_time: datetime | None = None

    @staticmethod
    def from_dict(dic):
        """从字典到对象"""
        if dic is None:
            return None
        return Student(**dic)
