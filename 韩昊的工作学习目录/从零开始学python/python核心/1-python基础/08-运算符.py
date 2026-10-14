"""
@Author  : 韩昊
@Company : *******
@Date    :
@Desc    :
@Version : 1.0
"""

#算术运算符 + - * / ** // %
print(1 + 2)   #3加
print (10 - 2) #8减
print(2 * 3)   #6乘
print(10 / 2)  #5.0 / 表示"真正的除法"，结果一定是浮点数，哪怕能整除 这样做是为了避免整数除法丢失小数的意外
#print(type(10 / 2)) # /结果是float
print(10 // 2) #5 //表示向下取整
#print(type(10 // 2)) # //结果是int
print (10 % 3) #取余数
print(10 **2)  #平方

#算符优先级
print("=" * 30)
print(10 +2 * 3) #16 不是36 （* / > + -)
#
print(10 + (2 * 3)) #16
print((10 + 2) * 3) #36 (先算括号里的 小括号的优先级最高
#格式化
print(f"10 / 3 = {10 / 3:.3f}")
print(f"{2 + 500:10}")
print(f"{10:%}")

print("=" * 30)
#赋值运算符号 =
a = 100
print(a)
a += 100
print(a)
a += 100
print(a)

print("=" * 30)
#比较运算符
#输出bool值 如果满足为True 不满足为False
print(10 > 5) #True
print(10 < 5) #False
print(10 >= 5)#True
print(10 <= 5)#False
print(10 == 5)#False
print(10 != 5)#True
print(10 != 10)# False