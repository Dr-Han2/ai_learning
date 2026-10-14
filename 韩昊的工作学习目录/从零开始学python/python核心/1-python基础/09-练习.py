"""
@Author  : 韩昊
@Company : *********
@Date    :
@Desc    :
@Version : 1.0
"""

APPLE_PRICE = 3.5
MILK_PRICE = 5.8

apple_count = input("请输入购买苹果的数量:") #input返回的是字符串
milk_count = input("请输入购买牛奶的数量")

apple_total_price = APPLE_PRICE * float(apple_count)
milk_total_price = MILK_PRICE * float(milk_count)

result = apple_total_price + milk_total_price
print(f"最终的花销是:{result}")