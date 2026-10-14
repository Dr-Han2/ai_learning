"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
import time


def counter(max_num):
    #定一个初始号
    num = 1
    #循环
    while num <= max_num:
        yield num #返回生成的排号,并暂停
        #增加号码
        num += 1

#创建一个生成器实例
gen = counter(5)
#生成第一个号
print(next(gen))
time.sleep(1)

print(next(gen))
time.sleep(1)

print(next(gen))
time.sleep(1)

print(next(gen))
time.sleep(1)

print(next(gen))
time.sleep(1)

