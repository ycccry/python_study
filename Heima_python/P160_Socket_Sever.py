import socket
import threading
import time
def send_fuc(conn):
    while True:
        send_msg = input('>>>')
        conn.send(send_msg.encode('UTF-8'))

def rece_fuc(conn):
    while True:
        rece_data = conn.recv(1024).decode('UTF-8')
        print(f'\n客户端:{rece_data}')
        if len(rece_data) == 0:
            break

if __name__ == '__main__':

    #定义一个Socket对象
    sk_sever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #创建服务端，并设置ip和端口
    sk_sever.bind(("localhost",8888))

    #设置可接受的链接数量
    sk_sever.listen(4)

    #accept()方法返回的是二元元组（链接对象，客户端地址信息）
    #也是阻塞方法，没有客户链接就停在这里
    # conn,address = sk_sever.accept()
    # print(f'接受到了客户端的链接，客户端的消息是:{address}')
    #接收客户端的消息，要使用客户端和服务端的本次链接对象，而非sk_sever对象
    #.recv(1024)是接收的参数是缓冲区的大小，一般给1024足矣
    #.decode，将传来的字节数据转换为字符串

    while True:
        conns, address = sk_sever.accept()
        # 定义接受和发送的双线程
        # 与服务端交互
        threading.Thread(target=rece_fuc,args=(conns,)).start()
        threading.Thread(target=send_fuc,args=(conns,)).start()
        print(f'接受到了客户端的链接，客户端的消息是:{address}')





