"""
@Author  : 韩昊
@Company : 未来元启
@Date    : 2026/10/13 16:00
@Version : 1.0
"""
from typing import Optional
from pydantic import BaseModel, Field


class CourseAddDTO(BaseModel):
    """新增课程参数模型"""
    name: str = Field(..., min_length=2, max_length=50, description="课程名称，2-50个字符")
    hour: int = Field(default=40, ge=1, le=500, description="课程学时，1-500")


class CourseUpdateDTO(BaseModel):
    """更新课程参数模型"""
    id: int = Field(..., gt=0, description="课程ID")
    name: Optional[str] = Field(None, min_length=2, max_length=50, description="课程名称")
    hour: Optional[int] = Field(None, ge=1, le=500, description="课程学时")