"""
@Author  : 刘光尘
@Company : 未来元启
@Date    : 2026/9/14 14:08
@Desc    : 
@Version : 1.0
"""
# 顶层业务异常（所有业务错误的父类）
class AppException(Exception):
    pass


# 参数错误
class ParamError(AppException):
    pass


# 权限错误
class PermissionError(AppException):
    pass

# 业务层错误
class ServiceError(AppException):
    pass

# 数据库错误
class DBError(AppException):
    pass
