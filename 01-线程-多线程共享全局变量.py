# 子线程里面的内容,可以访问到主线程中的全局变量;
# global: 如果声明的是复杂数据类型,不改变内存地址的情况下,就没有必要使用global


# import threading
#
# num1 = 111
# list1 = [1, 2, 3]
#
#
# # 获取全局变量的值
# def get_data():
#     print(num1, list1)
#
#
# # 改变全局变量的值
# def set_data():
#     # 改变全局变量要用global声明
#     global num1
#     # global list1
#     num1 = 222
#     list1.append('aaa')
#
#
# if __name__ == '__main__':
#     # 创建两个子线程
#     t1 = threading.Thread(target=get_data)
#     t2 = threading.Thread(target=set_data)
#
#     # 启动线程
#     t1.start()
#     t2.start()
#
#     # 查看值
#     print(num1, list1)

# first time

# import threading
#
#
# num = 100
# lu = [1, 2, 3, 4]
#
#
# def get_data():
#     print(num, lu)
#
#
# def change_data():
#     global num
#     num = 999
#     lu.append(num)
#     print(num, lu)
#
#
# if __name__ == '__main__':
#     _1thread = threading.Thread(target=get_data)
#     _2thread = threading.Thread(target=change_data)
#
#     _1thread.start()
#     _1thread.join()
#
#     _2thread.start()
#     _2thread.join()

# second time
# import threading
#
#
# num = 898
# _str = 'second time'
#
#
# def get_global_veriable():
#     print(num, _str)
#
#
# def change_global_veriable():
#     global num
#     num = 1000
#     _str1 = _str.replace('second', 'first')
#     print(num, _str1)
#
#
# if __name__ == '__main__':
#
#     _2thread = threading.Thread(target=get_global_veriable)
#     _3thread = threading.Thread(target=change_global_veriable)
#
#     _2thread.start()
#     _2thread.join()
#     _3thread.start()
#     _3thread.join()

# 第三遍
import threading


num = 100
tree = [[1, [3, [7, 9]]],
        [2],
        [[3, 5]], 0]


def get_global_veriable():
    print(num)
    print(tree[0][1][1])


def change_global_veriable():
    global num
    num = 10
    tree[1].insert(0, num)
    print(num, tree)


if __name__ == '__main__':
    threading.Thread(target=get_global_veriable).start()
    threading.Thread(target=change_global_veriable).start()