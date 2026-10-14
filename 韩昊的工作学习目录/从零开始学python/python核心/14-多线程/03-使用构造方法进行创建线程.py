"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
from threading import Thread
import time

#定义下载任务
def download(file_name,seconds):
    print(f"开始下载{file_name}")
    #模拟下载
    time.sleep(seconds)
    print(f"{file_name}下载完成")

#通过构造方法创建线程
thread1=Thread(target=download,args=("音乐1.mp4",3))
thread2=Thread(target=download,args=("音乐1.mp4",2))

#启动线程
#调用start()之和,会创建一个真正的系统线程,这个线程会参与CPU调用
# Python环境
thread1.start()
thread2.start()

#等待线程
thread1.join()
thread2.join()


print("\n程序运行完成")

