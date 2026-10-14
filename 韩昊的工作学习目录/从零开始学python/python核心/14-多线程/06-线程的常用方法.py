"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
import threading
import time

def download_file(file_name):
    print(f"[{threading.current_thread.name()}开始下载: {file_name}]")
    time.sleep(2)
    print(f"[{threading.current_thread.name()}下载完成:{file_name}]")

if __name__ == "__main__":
    t1 = threading.Thread(target=download_file,args=(1,))

