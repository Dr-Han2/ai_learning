"""
@Author  : 韩昊
@Company : ******
@Date    : 
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


# 数据库错误
class DBError(AppException):
    pass
#
def login(username):
    if not username:
        raise ParamError("用户名不能为空")
    if username != "admin":
        raise PermissionError("无权限访问")

try:
    login("")
except Exception as e:
    print("系统异常",e)
