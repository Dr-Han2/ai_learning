"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
import time
import threading

#定义一个任务
def task():
    #子线程(程序员手动创建的线程)
    while True:
        print("子线程中正在执行任务......")
        #让程序休眠1秒
        time.sleep(1)

#创建一个线程并绑定任务
therad = threading.Thread(target=task)
#启动线程
therad.start()

#在主线程中再定义一个死循环
while True:
    print("主线程中正在执行任务......")
    #让当前线程(主线程）休眠1秒
    time.sleep(1)
