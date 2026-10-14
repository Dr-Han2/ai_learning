"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
class BankAccount:
    #手续费 默认0.01
    __slots__ = ('__account_name', '__account_num', '__balance')
    __readonly__ = ('account_num', '_balance')
    service__fee_rate = 0.01

    #实例属性 account_num(账号) 、 balance(余额)
    def __init__(self,account_name,account_num,balance):
        self.__account_name=account_name
        self.__account_num = account_num
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance
