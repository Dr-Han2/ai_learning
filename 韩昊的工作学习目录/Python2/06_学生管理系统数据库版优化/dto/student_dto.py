"""
@Author  : 韩昊
@Company : 未来元启
@Date    : 2026/10/13 16:00
@Version : 1.0
"""
from typing import Optional
from pydantic import BaseModel, Field


class StudentAddDTO(BaseModel):
    """新增学生参数模型"""
    stu_num: str = Field(..., min_length=2, max_length=20, description="学生学号")
    name: str = Field(..., min_length=2, max_length=20, description="学生姓名")
    gender: str = Field(..., pattern="^[男女]$", description="性别，只能是 男 或 女")
    age: int = Field(..., ge=1, le=100, description="年龄，1-100")
    class_id: int = Field(..., gt=0, description="所属班级ID")
    phone: Optional[str] = Field(None, min_length=11, max_length=11, description="联系电话")


class StudentUpdateDTO(BaseModel):
    """更新学生参数模型"""
    id: int = Field(..., gt=0, description="学生ID")
    stu_num: Optional[str] = Field(None, min_length=2, max_length=20, description="学生学号")
    name: Optional[str] = Field(None, min_length=2, max_length=20, description="学生姓名")
    gender: Optional[str] = Field(None, pattern="^[男女]$", description="性别")
    age: Optional[int] = Field(None, ge=1, le=100, description="年龄")
    class_id: Optional[int] = Field(None, gt=0, description="所属班级ID")
    phone: Optional[str] = Field(None, min_length=11, max_length=11, description="联系电话")