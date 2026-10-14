"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
from dataclasses import dataclass
from datetime import datetime

@dataclass()
class Student:
    id: int | None = None
    name: str | None = None
    gender: str | None = None
    age: int  | None = None
    class_id: int| None = None
    phone: str | None = None
    create_time: datetime | None = None
    update_time: datetime | None = None

    @staticmethod
    def from_dict(dic):
        if dic is None:
            return None
        return Student(**dic)
