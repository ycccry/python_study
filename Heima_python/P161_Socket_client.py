import socket
import threading
import time
def send_fuc(sk_client):
    while True:
        send_msg = input('>>>')
        sk_client.send(send_msg.encode('UTF-8'))

def rece_fuc(sk_client):
    while True:
        rece_data = sk_client.recv(1024).decode('UTF-8')
        print(f'\n服务端:{rece_data}')
        if len(rece_data) == 0:
            break


if __name__ == '__main__':

    #定义一个Socket的客户端对象
    sk_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk_client.connect(('localhost',8888))

    #定义接受和发送的双线程
    threading.Thread(target=send_fuc,args=(sk_client,)).start()
    threading.Thread(target=rece_fuc,args=(sk_client,)).start()



