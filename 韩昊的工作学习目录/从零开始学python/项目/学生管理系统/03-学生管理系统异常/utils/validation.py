"""
@Author  : 刘光尘
@Company : 未来元启
@Date    : 2026/9/11 09:52
@Desc    : 
@Version : 1.0
"""
from exception import ParamError

# 定义一个电话号码校验函数
def check_phone_num(phone_num: str):
    """
    电话号码校验
    :param phone_num: 电话号码
    :return: True/False
    """
    # 不能为空
    if not phone_num.strip():
        # 抛出异常
        raise ParamError("电话号码不能为空")
    # 长度必须为11位
    if len(phone_num) != 11:
        raise ParamError("电话号码长度必须为11位")
    # 是否全是数字
    if not phone_num.isdigit():
        raise ParamError("电话号码必须全是数字")
    # 校验通过
    return True

if __name__ == '__main__':
    print(check_phone_num("13366669999"))
    print(check_phone_num("1336666999"))