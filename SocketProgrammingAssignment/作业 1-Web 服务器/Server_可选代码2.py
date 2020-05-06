# import socket module

from socket import *
from _thread import *
import threading

print_lock = threading.Lock()


def threaded(c):
    try:
        message = c.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        header = 'HTTP/1.1 200 OK \nConnection: close\n' + \
                 'Content0Length: {}\n'.format(len(outputdata)) + \
                 'Content-Type: text/html\n\n'
        c.send(header.encode())
        for i in range(0, len(outputdata)):
            c.send(outputdata[i].encode())
        c.close()
    except IOError:
        header = 'HTTP/1.1 404 Not Found'
        c.send(header.encode())
        c.close()


def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Prepare a server socket
    # Fill in start
    serverSocket.bind(('', 81))  # 使用 81 端口
    serverSocket.listen(1)
    # Fill in end

    while True:
        try:
            # Establish the connection
            print('Ready to server...')
            # Fill in start
            connectionSocket, addr = serverSocket.accept()
            # FIll in end
            start_new_thread(threaded, (connectionSocket,))
        except:
            print('Exit')

            break
    # 关闭服务端
    serverSocket.close()


if __name__ == '__main__':
    main()
