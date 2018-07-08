# 多线程实现对客户端数据的处理;
import socket
import threading


# 对于客户端 的处理单独封装一个函数
# def client_handler(service_client_socket, ip_port):
#     # 6.接收数据
#     str1 = service_client_socket.recv(1024)
#     print(ip_port, str1.decode('gbk'))
#     # 7.发送数据
#     service_client_socket.send('数据处理中......'.encode('utf-8'))
#     # 8.关闭套接字
#     service_client_socket.close()
#
#
# if __name__ == '__main__':
#     # 1.创建套接字
#     tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     # 2.端口复用
#     tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
#     # 3.绑定端口
#     tcp_socket.bind(("192.168.71.70", 8888))
#     # 4.变主动为被动
#     tcp_socket.listen(128)
#     # 5.死循环接收客户端的链接请求
#     while True:
#         service_client_socket, ip_port = tcp_socket.accept()
#         print(ip_port, '已链接...')
#
#         # 每次有一个客户端的链接发送过来以后,单独创建一个线程,对他进行数据的处理
#         t1 = threading.Thread(target=client_handler, args=(service_client_socket, ip_port))
#         # 主线程停止的时候,应该让子线程也停止!
#         # t1.setDaemon(True)
#         # 线程开启
#         t1.start()
#
#     # 不需要使用服务端的时候可以关闭tcp_socket
#     # tcp_socket.close()

# 第一遍
#
# def send_msg(backsoc):
#     print(backsoc.recv(1024).decode(encodin='utf-8'))
#     backsoc.send(input('send:').encode(encoding='utf-8'))
#     backsoc.close()
#
#
# if __name__ == '__main__':
#     Tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     Tcp_server.bind(('', 9905))
#     Tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
#     Tcp_server.listen(128)
#
#     while True:
#         backsoc, IP_port = Tcp_server.accept()
#
#         thread1 = threading.Thread(target=send_msg, args=(backsoc,))
#         thread1.setDaemon(True)
#         thread1.start()
#     Tcp_server.close()

# second time

def send_msg(child_server):
    print(child_server.recv(1024).decode(encoding='utf-8'))
    child_server.send(input('anwser:').encode(encoding='utf-8'))
    child_server.close()


if __name__ == '__main__':
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.bind(('', 9002))
    tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server.listen(128)
    while True:
        child_server, IP_port = tcp_server.accept()
        child_thread = threading.Thread(target=send_msg, args=(child_server,))
        child_thread.setDaemon(True)
        child_thread.start()

    tcp_server.close()