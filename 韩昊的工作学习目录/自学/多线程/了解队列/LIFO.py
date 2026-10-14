"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
import queue

queue1 =queue.LifoQueue()

queue1.put(1)
queue1.put(2)
queue1.put(3)

print(queue1.get())
print(queue1.get())
print(queue1.get())
