"""
@Author  : 韩昊
@Company : 未来元启
@Date    : 2026/10/13 16:00
@Version : 1.0
"""
from pydantic import BaseModel, Field
from datetime import date


class ScoreAddDTO(BaseModel):
    """新增成绩参数模型"""
    stu_id: int = Field(..., gt=0, description="学生ID")
    course_id: int = Field(..., gt=0, description="课程ID")
    score: float = Field(..., ge=0, le=100, description="分数，0-100")
    exam_time: date = Field(None, description="考试日期，格式 YYYY-MM-DD")


class ScoreUpdateDTO(BaseModel):
    """更新成绩参数模型"""
    id: int = Field(..., gt=0, description="成绩ID")
    score: float = Field(..., ge=0, le=100, description="分数，0-100")
    exam_time: date = Field(None, description="考试日期")