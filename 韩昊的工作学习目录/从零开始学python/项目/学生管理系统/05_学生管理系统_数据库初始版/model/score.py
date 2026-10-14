"""
@Author  : hanhao
@Company : 未来元启
@Date    : 2026/10/9 10:18
@Desc    : 
@Version : 1.0
"""
from dataclasses import dataclass
from datetime import datetime, date

@dataclass
class Score:
    """成绩类"""
    id: int | None= None
    stu_id: int | None= None
    course_id: int | None= None
    score: float | None= None
    exam_time: date | None= None
    create_time: datetime | None= None
    update_time: datetime | None= None

    @staticmethod
    def from_dict(dic):
        """从字典到对象"""
        if dic is None:
            return None
        return Score(**dic)
