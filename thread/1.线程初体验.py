import threading
import time


def print_numbers():
    for i in range(10):
        time.sleep(1)
        print(i)


if __name__ == '__main__':
    # 创建线程
    th = threading.Thread(target=print_numbers)
    # 启动线程
    th.start()
    # 等待线程结束
    th.join()
