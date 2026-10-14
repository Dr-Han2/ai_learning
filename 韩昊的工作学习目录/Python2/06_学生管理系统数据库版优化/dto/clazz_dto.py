"""
@Author  : 韩昊
@Company : 未来元启
@Date    : 2026/10/12 16:36
@Version : 1.0
"""
from typing import Optional
from pydantic import BaseModel, Field


class ClazzAddDTO(BaseModel):
    """新增班级参数模型"""
    name: str = Field(..., min_length=2, max_length=50, description="班级名称，必填，2-50个字符")
    teacher_name: str = Field(..., min_length=2, max_length=30, description="班主任姓名，必填，2-30个字符")


class ClazzUpdateDTO(BaseModel):
    """更新班级DTO"""
    id: int = Field(..., gt=0, description="班级ID")
    name: Optional[str] = Field(None, min_length=2, max_length=50, description="班级名称")
    teacher_name: Optional[str] = Field(None, min_length=2, max_length=30, description="班主任姓名")