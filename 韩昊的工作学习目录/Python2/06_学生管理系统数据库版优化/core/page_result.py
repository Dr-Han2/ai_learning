"""
@Author  : 韩昊
@Company : 未来元启
@Date    : 2026/10/13 11:44
@Version : 1.0
"""
from pydantic import BaseModel, Field
from typing import TypeVar, Generic, List

from core.page_request import PageRequest

# 定义泛型
T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    """分页结果类"""
    total_record: int = Field(..., ge=0, description="符合查询条件的总记录数")
    total_page: int = Field(..., ge=0, description="符合查询条件的总页数")
    page_num: int = Field(..., ge=1, description="当前页号")
    page_size: int = Field(..., ge=1, le=100, description="每页数量")
    rows: List[T] = Field(default_factory=list, description="当前页数据")

    @classmethod
    def empty(cls, page_req: PageRequest) -> "PageResult[T]":
        """返回空结果"""
        return PageResult[T](
            total_record=0,
            total_page=0,
            page_num=page_req.page_num,
            page_size=page_req.page_size,
            rows=[]
        )

    @classmethod
    def of(cls, page_req: PageRequest, total_record: int, rows: List[T]) -> "PageResult[T]":
        """静态工厂方法"""
        total_page = PageResult._calculate_total_page(total_record, page_req.page_size)
        return PageResult[T](
            total_record=total_record,
            total_page=total_page,
            page_num=page_req.page_num,
            page_size=page_req.page_size,
            rows=rows
        )

    @staticmethod
    def _calculate_total_page(total_record: int, page_size: int):
        if total_record <= 0:
            return 0
        if page_size <= 0:
            return 0
        if (total_record % page_size) == 0:
            return total_record // page_size
        else:
            return total_record // page_size + 1