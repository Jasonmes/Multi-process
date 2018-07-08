# 模块名: multiprocessing
import multiprocessing
import time


# 上传内容
def upload(num):
    print(multiprocessing.current_process())
    for i in range(num):
        print('上传...', i+1)
        time.sleep(0.1)


def download(name, age, address):
    print(multiprocessing.current_process())
    print(name, age, address)


if __name__ == '__main__':
    # 创建两个子进程
    #  上传单独使用一个子进程
    p1 = multiprocessing.Process(target=upload, name='aaa', args=(3, ))
    #  下载单独使用一个子进程
    p2 = multiprocessing.Process(target=download, name='bbb', kwargs={'name': '李四', 'age': 20, 'address': '三里屯...'})

    # 进程使用,需要开启
    p1.start()
    p2.start()
