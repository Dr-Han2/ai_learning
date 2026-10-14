"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
import threading

def task():
    print("线程开始任务")

#定义线程并绑定任务
thread1 = threading.Thread(target=task)

#启动线程
thread1.start()