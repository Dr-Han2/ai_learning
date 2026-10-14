"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
#常见数据结构 先进先出FIFO
#导入python的queue模块
#创建一个空队列
import queue
queue1 = queue.Queue()

#添加元素
queue1.put(1)
queue1.put(2)
queue1.put(3)

print(queue1.get()) #取出并移除元素
print(queue1.get())
print(queue1.get())
print(queue1.empty()) #判断是否为空
queue1.put(4)
print(queue1.empty())
print(queue1.full())
