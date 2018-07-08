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

    # 进程使用,需要开启
    p1.start()
    p2.start()
