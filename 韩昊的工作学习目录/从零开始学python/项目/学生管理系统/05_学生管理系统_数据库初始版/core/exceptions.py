"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
class AppException(Exception):
    """当前系统异常基类"""

    def __init__(self, message="系统异常", code=500, data=None):
        super().__init__(message)
        self.message = message  # 异常信息
        self.code = code  # 异常码，根据自己项目的实际情况定义
        self.data = data or {}  # 异常数据

    def to_dict(self):
        """转换为字典（用于API响应）"""
        return {
            "code": self.code,
            "message": self.message,
            "data": self.data
        }


# ============ 业务异常（4xx）Service层的异常基类 ============
class BusinessException(AppException):
    """业务异常基类"""

    def __init__(self, message="业务异常", code=400, data=None):
        super().__init__(message, code, data)


class NotFoundError(BusinessException):
    """资源不存在"""

    def __init__(self, resource="资源", resource_id=None):
        if resource_id:
            message = f"{resource} ID = {resource_id} 不存在"
        else:
            message = f"{resource} 不存在"
        super().__init__(message, code=404, data={"resource": resource, "resource_id": resource_id})


class AlreadyExistsError(BusinessException):
    """资源已存在"""

    def __init__(self, resource="资源", field=None, value=None):
        if field and value:
            message = f"{resource} 的 {field} '{value}' 已存在"
        else:
            message = f"{resource} 已存在"
        super().__init__(message, code=409, data={"resource": resource, "field": field, "value": value})


class ValidationError(BusinessException):
    """数据校验失败"""

    def __init__(self, message="数据校验失败", field=None, value=None):
        if field and value:
            message = f"字段 {field} 的值 '{value}' 无效"
        super().__init__(message, code=400, data={"field": field, "value": value})


class OperationFailedError(BusinessException):
    """操作失败"""

    def __init__(self, operation="操作", reason=None):
        if reason:
            message = f"{operation} 失败: {reason}"
        else:
            message = f"{operation} 失败"
        super().__init__(message, code=400, data={"operation": operation, "reason": reason})


# ============ 系统异常（5xx）DAO层的异常基类 ============

class SystemException(AppException):
    """系统异常基类"""

    def __init__(self, message="系统异常", code=500, data=None):
        super().__init__(message, code, data)


class DatabaseError(SystemException):
    """数据库异常"""

    def __init__(self, message="数据库操作失败"):
        super().__init__(message, code=500)


class ConfigError(SystemException):
    """配置异常"""

    def __init__(self, key=None):
        if key:
            message = f"配置项 {key} 无效或缺失"
        else:
            message = "配置错误"
        super().__init__(message, code=500, data={"key": key})


# ============ 权限异常（401/403） ============

class UnauthorizedError(AppException):
    """未认证（未登录）"""

    def __init__(self, message="请先登录"):
        super().__init__(message, code=401)


class ForbiddenError(AppException):
    """无权限"""

    def __init__(self, message="权限不足"):
        super().__init__(message, code=403)