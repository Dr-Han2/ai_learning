"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
#线程语法
#thread.start_new)thread(function, args[, kwargs])
#参数说明 function:线程函数 args:传递给线程函数的参数 必须是tuple
#kwargs-可选参数
import _thread
import time

#定义一个输出时间的函数
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print ("%s:%s"%(threadName, time.ctime(time.time())))


try:
    _thread.start_new_thread(print_time, ("Thread-1", 2,))
    _thread.start_new_thread(print_time, ("Thread-2", 4,))
except:
    print("\n")
    "Error: unable to start thread"

while 1:
    pass

