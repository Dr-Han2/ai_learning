"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
class PasswordLenghtException(Exception):
    pass

password =input("请输入您的密码")

if not password or password == "":
    raise PasswordLenghtException("密码不能为空")

if len(password) < 6:
    raise PasswordLenghtException("密码长度不能小于6位数")