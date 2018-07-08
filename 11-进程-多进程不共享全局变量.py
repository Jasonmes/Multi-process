# 多进程不共享全局变量,在使用到全局变量的时候,自己的进程中会自己创建一份儿
import multiprocessing

num1 = 111
list1 = [1, 2, 3]


# 获取
def get_data():
    print(num1, list1)


# 设置
def set_data():
    global num1
    num1 = 222
    list1.append('aaa')
    # 打印set之后的值
    print('set之后的值: ', num1, list1)


if __name__ == '__main__':
    # 创建两个子进程
    # 先设置
    p1 = multiprocessing.Process(target=set_data)
    # 在获取
    p2 = multiprocessing.Process(target=get_data)

    # 开启进程
    p1.start()
    p2.start()

    # 进程等待
    p1.join()
    p2.join()

    print('最终结果: ', num1, list1)

