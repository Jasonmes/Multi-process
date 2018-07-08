# # 1.引入模块
# import socket
# import threading
#
#
# # 发送数据
# def send_msg(udp_socket, tuple2):
#     str1 = input('输入发送的信息: ')
#     udp_socket.sendto(str1.encode('utf-8'), tuple2)
#
#
# # 接收数据
# def receive_msg(udp_socket):
#     while True:
#         str2, tuple3 = udp_socket.recvfrom(1024)
#         print(tuple3, str2.decode('gbk'))
#
#
# # 主要逻辑封装到一个函数中
# def main():
#     # 2.创建套接字
#     udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     udp_socket.bind(('', 9999))
#
#     # 确定好了给谁发
#     tuple2 = (input('请输入对方的IP: '), int(input('请输入对方的端口号(1024-65535): ')))
#     # 以一个单独的子线程接收数据(死循环接收)
#     t1 = threading.Thread(target=receive_msg, args=(udp_socket, ))
#     t1.setDaemon(True)
#     t1.start()
#
#     # 3.循环发送和接收数据
#     while True:
#         # 选择先发送,发一条,收一条;  或者跳出程序
#         flag = input('输入1就是发送并接收数据, 输入2就是退出: ')
#         # 判断:
#         if flag == '1':
#             # 数据发送
#             send_msg(udp_socket, tuple2)
#
#         elif flag == '2':
#             # 退出程序
#             print('聊天结束!')
#             break
#         else:
#             print('没有此功能!!!')
#             continue
#
#     # 4.关闭套接字
#     udp_socket.close()
#
#
# # 程序入口
# if __name__ == '__main__':
#     main()

# first time
# first time
import socket
import threading

#
# def send_msg(local_chat, friends_IP_PORT):
#     local_chat.sendto(input('send a word:').encode(encoding='utf-8'), friends_IP_PORT)
#
#
#
# def receive_msg(local_chat):
#     while True:
#         print(local_chat.recvfrom(1024)[0].decode(encoding='utf-8'))
#
#
# if __name__ == '__main__':
#
#     local_chat = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     local_chat.bind(('', 8989))
#     local_chat.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
#     friends_IP_PORT = (input('IP:'), int(input('PORT:')))
#
#     friend_talk = threading.Thread(target=receive_msg, args=(local_chat,))
#     friend_talk.setDaemon(True)
#     friend_talk.start()
#
#     while True:
#         choices = int(input('1/2?:'))
#         if choices == 1:
#             send_msg(local_chat, friends_IP_PORT)
#
#         else:
#             local_chat.close()
#             break

# second time
def send_msg(local_chat, fri_iP_port):
    local_chat.sendto(input('send to fri:'), fri_iP_port)


def receive_msg(local_chat):
    while True:
        print(local_chat.recvfrom(1024)[0].decode(encoding='utf-8'))


def main():
    local_chat = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    local_chat.bind(('', 9012))
    local_chat.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    fri_iP_port = (input("IP:"), int(input("PORT:")))

    fri_thread = threading.Thread(target=receive_msg, args=(local_chat,))
    fri_thread.setDaemon(True)
    fri_thread.start()

    while True:
        choices = int(input('1/2?:'))
        if choices == 1:
            send_msg(local_chat, fri_iP_port)
        else:
            print('wrong')
            break
    local_chat.close()


if __name__ == '__main__':
    main()