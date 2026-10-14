"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
import queue
#非阻塞获取(避免死锁)
queue1 = queue.Queue(maxsize=3)
queue1.put(1)
queue1.put(2)
queue1.put(3)

try:
    item = queue1.get_nowait() #等待 等价于q.get(block=False)
except queue.Empty:
    print("队列为空")