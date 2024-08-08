import threading
import time

thread_lock = threading.Lock()


class MyThread(threading.Thread):
    def __init__(self, threadId, name, delay):
        super(MyThread, self).__init__()
        self.threadId = threadId
        self.name = name
        self.delay = delay

    def run(self):
        while True:
            thread_lock.acquire()
            print_time(self.name)
            thread_lock.release()
            time.sleep(1)


def print_time(name: str):
    print(name)


# 创建新线程
thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
