# 锁机制(同步锁): 线程在使用全局变量的时候,用的时候锁住,不用的时候解锁...
import threading

num1 = 0
# 模块中有一个类Lock
lock = threading.Lock()


# 操作全局变量
def add_num():
    global num1
    for i in range(1000000):
        # 真正操作全局变量的时候,在锁住
        # lock.acquire()
        num1 += 1
        print(num1)
        # 操作完成释放锁
        # lock.release()


if __name__ == '__main__':
    # 创建两个子线程
    t1 = threading.Thread(target=add_num)
    t2 = threading.Thread(target=add_num)

    # 开启线程
    t1.start()
    t2.start()

    # t1和t2结束以后在打印最终结果
    t1.join()
    t2.join()

    # 打印结果
    print(num1)
