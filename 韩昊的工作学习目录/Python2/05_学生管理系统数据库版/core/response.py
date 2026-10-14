"""
@Author  : 韩昊
@Company : 未来元启
@Date    : 2026/10/12 16:15
@Version : 1.0
"""
from typing import TypeVar, Generic, Optional
from pydantic import BaseModel, Field

# 定义泛型
T = TypeVar("T")


class Response(BaseModel, Generic[T]):
    """公共返回信息"""
    code: int = Field(0, description="状态码，0表示成功")
    message: str = Field("成功", description="提示信息")
    data: Optional[T] = Field(None, description="返回数据")

    @classmethod
    def success(cls, data: Optional[T] = None, message: str = "成功") -> "Response[T]":
        """成功响应"""
        return cls(code=0, message=message, data=data)

    @classmethod
    def error(cls, code: int = 400, message: str = "error", data: Optional[T] = None) -> "Response[T]":
        """错误响应"""
        return cls(code=code, message=message, data=data)

    @classmethod
    def not_found(cls, message: str = "资源不存在") -> "Response[T]":
        """404 响应"""
        return cls(code=404, message=message, data=None)

    @classmethod
    def unauthorized(cls, message: str = "未授权") -> "Response[T]":
        """401 响应"""
        return cls(code=401, message=message, data=None)

    @classmethod
    def forbidden(cls, message: str = "禁止访问") -> "Response[T]":
        """403 响应"""
        return cls(code=403, message=message, data=None)

    @classmethod
    def validation_error(cls, message: str = "参数验证失败") -> "Response[T]":
        """422 响应"""
        return cls(code=422, message=message, data=None)