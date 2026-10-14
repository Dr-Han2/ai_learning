"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
#生成器推导式
gen = (x for x in range(10))
print(type(gen))

#遍历生成器
print(next(gen))
print(next(gen))
print(next(gen))
#yield return 都能返回数据
#teturn 会直接结束函数
# yield会暂停函数,记住当前执行位置 下次调用从这里继续
#直到无yield -> 抛出 StopIteration
#调用一次 走一步,停一步,记住位置,续着走

