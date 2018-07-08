# 模块名: multiprocessing
import multiprocessing
import time


# 上传内容
def upload():
    for i in range(5):
        print('上传...', i+1)
        time.sleep(0.1)


def download():
    for i in range(5):
        print('下载电影.......', i+1)
        time.sleep(0.1)


if __name__ == '__main__':
    # 创建两个子进程
    #  上传单独使用一个子进程
    p1 = multiprocessing.Process(target=upload)
    #  下载单独使用一个子进程
    p2 = multiprocessing.Process(target=download)

    # 3.守护进程(不是方法,而是属性)
    # p1.daemon = True
    # p2.daemon = True

    # 进程使用,需要开启
    p1.start()
    p2.start()

    # 2.进程等待
    # p1.join()
    # p2.join()

    # 1.主进程默认和子进程一起执行: 子进程想要执行需要去cup索要资源就会让主进程里面的代码多走一会儿
    #       主进程走完以后,等待子进程全部执行完毕在停止!
    # 2.进程等待: 主进程等待子进程完成以后在继续执行
    # 3.守护进程: 主进程执行完毕, 子进程无条件停止
    # time.sleep(0.2)

    print('主进程里面的代码执行完毕了....')
