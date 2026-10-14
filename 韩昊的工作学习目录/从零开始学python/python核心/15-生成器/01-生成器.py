"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
import time


#定义一个生成器
def my_generator():
    print("生成第一个数") #返回1 然后暂停 ,并且要记住当前执行的位置
    yield 1
    print("生成第二个数")
    yield 2
    print("生成第三个数")
    yield 3

#实例化一个生成器
gen = my_generator()
print(type(gen))



print(next(gen))
time.sleep(1)
print(next(gen))
time.sleep(1)
print(next(gen))
time.sleep(1)

#print(next(gen))
#time.sleep(1)         #StopIteratio异常


#调用前先获取一个生成器的实例
#再用next(生成器实例)获取值
