"""
@Author  : 韩昊
@Company : 未来元启
@Date    : 2026/10/13 11:13
@Version : 1.0
"""
from pydantic import BaseModel, Field, field_validator
import re


class PageRequest(BaseModel):
    """分页请求类"""
    page_num: int = Field(default=1, ge=1, description="当前页码")
    page_size: int = Field(default=10, ge=1, le=100, description="每页大小")
    order_by: str = Field("update_time", description="排序字段")
    is_asc: bool = Field(default=True, description="是否升序")

    @field_validator("order_by")
    @classmethod
    def validate_order_by(cls, value):
        """对order_by字段进行特殊校验"""
        if value is None or value.strip() == "":
            return "update_time"
        if value and not re.match(r"^[a-zA-Z0-9_]+$", value):
            return "update_time"
        return value

    @property
    def offset(self):
        """计算分页查询时的起始位置（偏移量）"""
        return (self.page_num - 1) * self.page_size

    @property
    def sort(self):
        """计算分页查询时的排序字段"""
        return "ASC" if self.is_asc else "DESC"