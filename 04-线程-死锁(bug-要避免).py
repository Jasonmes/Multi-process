# 锁住全局变量以后,忘记解锁了...
# import threading
#
#
# list1 = ['a', 'b', 'c', 'd', 'e']
# lock = threading.Lock()
#
#
# # 定义一个函数,根据线程的顺序号,获取列表中的元素
# def get_ele(index):
#     # 我这个线程操作的时候,其他线程只能看着
#     lock.acquire()
#     # 获取元素的时候，索引值不能超过列表的长度
#     if index >= len(list1):
#         print(index, '传递过来的参数,超过最大索引值,列表中没有该元素...')
#         # 如果超出了,下面就不要在打印了,return退出
#         lock.release()  # 不写这句就是死锁...
#         return
#     print(list1[index])
#     # 我操作完毕，其他线程才能操作...
#     lock.release()
#
#
# if __name__ == '__main__':
#     # 创建10个子线程,每个线程都去list1中获取自己对应顺序号的元素;
#     for i in range(10):
#         t1 = threading.Thread(target=get_ele, args=(i, ))
#         t1.start()

# first time
# import threading
#
# lock_list = threading.Lock()
#
# _1list = [1, 2, 34, 5, 6, 78, 765]
#
#
# def change_global_list(num):
#     lock_list.acquire()
#     if num > len(_1list) - 1:
#         print('wrong')
#         lock_list.release()
#         return
#     else:
#         print(_1list[num])
#         lock_list.release()
#
#
# if __name__ == '__main__':
#     threading.Thread(target=change_global_list, args=(int(input('which num you want:')),)).start()

# second time
# import threading
#
#
# _2list = [12, 2, 34, 5, 67, 6, 54]
# lock_list = threading.Lock()
#
#
# def change_global_list(num):
#     lock_list.acquire()
#     if num > len(_2list) - 1:
#         print('wrong')
#         lock_list.release()
#         return
#     else:
#         print(_2list[num])
#         lock_list.release()
#
#
# if __name__ == '__main__':
#     threading.Thread(target=change_global_list, args=(int(input(':')),)).start()

# third time
import threading

_3lock_list = threading.Lock()
_3list = [2, 3, 40, 5, 43, 39, 98, 765, 4]


def change_global_list(num):
    _3lock_list.acquire()
    if num > len(_3list) - 1:
        print('out of index')
        _3lock_list.release()
        return
    else:
        print(_3list[num])
        _3lock_list.release()


if __name__ == '__main__':
    threading.Thread(target=change_global_list, args=(int(input('which num you want:')),)).start()






