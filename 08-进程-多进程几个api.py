# 模块名: multiprocessing
import multiprocessing
import time
import os
import signal


# 上传内容
def upload():
    # 子进程1
    # print(multiprocessing.current_process())
    # 可以通过进程编号,从进程内部来关闭进程
    #       进程对象.pid： 进程的编号;
    print(multiprocessing.current_process().pid)
    # os.getpid(); 当前进程编号;
    # os.getppid();父进程编号
    print(os.getpid(), os.getppid())

    for i in range(5):
        print('上传...', i+1)
        time.sleep(0.1)
        # 可以打印一次就关闭进程1
        #  用signal模块中的常量SIGKILL;  9
        os.kill(os.getpid(), signal.SIGKILL)
        # os.kill(os.getpid(), 9)


def download():
    # 子进程2
    # print(multiprocessing.current_process())
    for i in range(5):
        print('下载电影.......', i+1)
        time.sleep(0.1)


if __name__ == '__main__':

    # 1.当前进程
    # print(multiprocessing.current_process())

    # 创建两个子进程
    #  上传单独使用一个子进程
    p1 = multiprocessing.Process(target=upload)
    #  下载单独使用一个子进程
    p2 = multiprocessing.Process(target=download)

    # 进程使用,需要开启
    p1.start()
    p2.start()

    # 3.从外部,关闭进程
    # time.sleep(0.2)
    # p1.terminate()


    # 2.活动进程列表(子进程)
    # print(multiprocessing.active_children())
