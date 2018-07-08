# 同一时间,谁先操作...

# 获取全局变量的时候,多个子线程获取的是同一个时间点的值,那么就容易出问题;
#   应该是一个线程操作的时候另一个线程看着...

# import threading
#
# num1 = 0
#
#
# # 操作全局变量
# def add_num():
#     global num1
#     for i in range(100):
#         num1 += 1
#
#
# if __name__ == '__main__':
#     # 创建两个子线程,都给num1增加值
#     t1 = threading.Thread(target=add_num)
#     # t2 = threading.Thread(target=add_num)
#
#     # 开始线程
#     t1.start()
#     # t2.start()
#
#     # 保证两个子线程执行完毕以后,在打印
#     t1.join()
#     # t2.join()
#
#     # 打印最终结果
#     print(num1)

# first time
import threading

# tree = [[8, [9, [10, 0]]],
#         [1, [0, 5]],
#         [0, 7],
#         [[4, 9], [2, 3]]]
#
#
# def change_global_tree(num):
#     tree[3][1].insert(1, num)
#     print(tree)
#
#
# if __name__ == '__main__':
#     # args is tuple
#     threading.Thread(target=change_global_tree, args=(int(input('insert num:')),)).start()
#     threading.Thread(target=change_global_tree, args=(int(input('insert num:')),)).start()


# second time and third time
import threading


tree = [2,
        [3, [7, [8, 9], 1]],
        [8, 0],
        [9],
        [12],
        [45, [33, 21]]]


def change_global_tree(num):
    tree[1][1][1].insert(1, num)
    print(tree)


if __name__ == '__main__':
    threading.Thread(target=change_global_tree, args=(int(input('insert num:')),)).start()
    threading.Thread(target=change_global_tree, args=(int(input('insert num:')),)).start()


def change_global_tree():
    pass


if __name__ == '__main__':
    threading.Thread(target=change_global_tree, args=(int(input('insert num:')),)).start()
    threading.Thread(target=change_global_tree, args=(int(input('insert num:')),)).start()