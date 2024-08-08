import threading
import time

exitFlag = False


class MyThread(threading.Thread):
    def __init__(self, threadId, name, delay):
        super(MyThread, self).__init__()
        self.threadId = threadId
        self.name = name
        self.delay = delay

    def run(self):
        print("开始线程：" + self.name)
        print_time(self.name, self.delay)


def print_time(name: str, delay: int):
    time.sleep(delay)
    while not exitFlag:
        print("{}_{}".format(name, time.time()))


if __name__ == '__main__':
    thread1 = MyThread(1, "Thread-1", 0.2)
    thread2 = MyThread(2, "Thread-2", 0.3)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()