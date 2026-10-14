"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
import queue
#(priority,data),优先级越小越先出队
#格式 priorityqueue1.put((优先级,数据))
priorityqueue1 = queue.PriorityQueue()
priorityqueue1.put((1,"low"))
priorityqueue1.put((0,"high"))
print(priorityqueue1.get())
#Output:(优先级,数据)