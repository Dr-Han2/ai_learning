"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
import threading
import time


def print_time(thread_name, delay):
    for count in range(5):
        time.sleep(delay)
        print(f"{thread_name}: {time.ctime(time.time())}")


def main():
    threads = [
        threading.Thread(target=print_time, args=("Thread-1", 2)),
        threading.Thread(target=print_time, args=("Thread-2", 4)),
    ]

    try:
        for t in threads:
            t.start()
    except RuntimeError as e:
        print(f"Error: unable to start thread - {e}")
        return

    # 等待所有子线程结束（替代 while 1: pass 的忙等）
    for t in threads:
        t.join()

    print("所有线程结束")


if __name__ == "__main__":
    main()