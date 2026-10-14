"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
from threading import Thread
import  time

class DownLoadThread(Thread):
    #使用构造方法
    def __init__(self,file_name,seconds):
        #调用父类构造方法
        super().__init__()
        #自定义的属性,接收参数
        self.file_name = file_name
        self.seconds = seconds

    #重写run()方法 自定义线程任务
    def run(self):
        print(f"开始下载{self.file_name}")
        # 模拟下载
        time.sleep(self.seconds)
        print(f"{self.file_name}下载完成")

#创建自定义线程
thread1 = DownLoadThread("电影1.MP4",3)
thread2 = DownLoadThread("电影2.MP4",2)


