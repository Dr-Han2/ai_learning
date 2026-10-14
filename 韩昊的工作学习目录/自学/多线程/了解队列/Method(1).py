"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
import queue

#优先级任务处理
queue1 =queue.PriorityQueue()

queue1.put((3,"Scan"))
queue1.put((1,"Emergency"))
queue1.put((2,"Log"))

while not queue1.empty():
    print(queue1.get())