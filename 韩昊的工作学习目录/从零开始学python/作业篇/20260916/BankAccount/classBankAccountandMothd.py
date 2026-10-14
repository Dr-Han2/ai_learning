"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
#定义一个BankAccount类
#1 类属性 是写在类里 方法外
#如 前文的school_name
class BankAccount:
    #手续费 默认0.01
    service__fee_rate = 0.01

    #实例属性 account_num(账号) 、 balance(余额)
    def __init__(self,account_name,account_num,balance):
        self.account_name=account_name
        self.account_num = account_num
        self.balance = balance

    #为方便调试和打印对象信息 我们定义一个魔术方法
    def __repr__(self):
        return f"姓名:{self.account_name}\n账号:{self.account_num}\n余额:{self.balance}元"
#测试打印用户信息 成功
#zhang_san =BankAccount("张三",1001200230034004,100)
#print(zhang_san)
    #取款功能

    def withdraw(self,amount):
        #若amount<=0 余额不足 无法取款
        if amount <= 0:
            print("取款金额必须大于0!")
            return
        #扣除金额+手续费
        #手续费
        fee = amount * self.service__fee_rate
        #扣除总金额
        total =amount + fee

        if total > self.balance:
            print(f"当前余额不足,您当前余额{self.balance:.2f},取款{amount:.2f},总扣除{total},包含手续费{fee:.2f}")
        else:
            self.balance -= total
            print(f"取款成功！请取出: {amount:.2f}, 扣除手续费: {fee:.2f}, 剩余余额: {self.balance:.2f}")

    @classmethod
    #设置手续费
    def set_service_fee(clc,rate):
        if 0 <= rate <= 0.1:
            clc.service__fee_rate = rate
            print(f"手续费比例设置成功:{rate}")
        else:
            print(f"手续费必须在0到0.1之间,您输入的是{rate:.2f}")

    def verify_card(card_num):
        if isinstance(card_num,str) and len(card_num) == 16 and card_num.isdigit():
            return True
        return False












