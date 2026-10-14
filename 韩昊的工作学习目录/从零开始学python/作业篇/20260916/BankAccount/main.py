"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
from classBankAccountandMothd import BankAccount

if __name__ == '__main__':
    #实例化两个用户
    account1 = BankAccount("张三 ","1002200330044005",10000)

    account2 = BankAccount("李四","1001200230034004",5000)

    #1初始化用户信息
    print(repr(account1))
    print(repr(account2))

    #2设置手续费
    BankAccount.set_service_fee(0.02)
    print()
    # 3. 验证卡号（静态方法，通过类名调用）
    print(f"银行卡号验证:{BankAccount.verify_card(account1.account_num)}")
    #取款
    print("account1取款:1000元")
    account1.withdraw(1000)
