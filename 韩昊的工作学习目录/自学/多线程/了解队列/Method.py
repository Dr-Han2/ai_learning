"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
#put(item,block=True,timeout=None)
#将item放入队列 如果block为True且队列已满,则等待timeout秒,直到队列有空闲
#空间,如果timeout为None,则无限等待

#get(block=True, timeout=None)
#从队列中获取并移除一个元素。如果 block 为 True 且队列为空，则等待 timeout 秒，直到队列中有元素。如果 timeout 为 None，则无限等待。

#qsize()
#返回队列中的元素数量。

#empty()
#如果队列为空，返回 True，否则返回 False。

#full()
#如果队列已满，返回 True，否则返回 False。
import queue,threading

queue1= queue.Queue(maxsize=3)#(容量为3的队列)

#生产者-消费者模型
def producer():
    for i in range(5):
        queue1.put(f"Task-{i}")
        print(f"Producer:Task-{i}")
def consumer():
    while True:
        item = queue1.get()
        print(f"Consumer:{item}")
        queue1.task_done()
threading.Thread(target=producer,daemon=True).start()
threading.Thread(target=consumer,daemon=True).start()
queue1.join()
