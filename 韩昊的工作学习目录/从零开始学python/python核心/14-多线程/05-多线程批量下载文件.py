"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
from threading import Thread
import time

def download(file_name,seconds):
    print(f"开始下载{file_name}")
    #模拟下载时间
    time.sleep(seconds)
    print(f"{file_name}下载完成")

#
file_list =["电影1.mp4","电影2.mp4","电影3.mp4","电影4.mp4"]
#保存创建好的线程,用于阻塞等待
threads=[]

#遍历列表,每个文件创建一个线程, 进行文件等待
for file_name in file_list:
    #创建线程
    thread = Thread(target=download,args=(file_name,2))
    #启动线程
    thread.start()
    #线程加入列表
    threads.append(thread)

#阻塞等待线程结束
for thread in threads:
    thread.join()

#结果
print("所有任务完成")
