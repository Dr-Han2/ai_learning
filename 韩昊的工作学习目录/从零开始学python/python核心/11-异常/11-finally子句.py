"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
# 接收用户输入的两个数，进行除尘运算
try:
    num1 = float(input("请输入第一个数字："))
    num2 = float(input("请输入第二个数字："))
    print(f"{num1} / {num2} = {num1 / num2}")
except Exception as e:
    print(f"查看异常详细信息：{e}")
else:  # 不推荐
    print("没有异常")
finally:
    print("无论是否有异常都会执行")