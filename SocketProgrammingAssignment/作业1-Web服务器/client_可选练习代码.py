import sys
from socket import *
##to run the programme in cmd:
#cd Desktop\code\network_coding_by_python\HttpAgent.py 127.0.0.1 800 HelloWorld.html
serverName=sys.argv[1] #sever name,here is my ip address
serverPort=int(sys.argv[2]) #any port consistent with the server end
filename=sys.argv[3]
request_head_1='GET /'
request_head_2=' HTTP/1.1\nHost: 127.0.0.1:48\nConnection: keep-alive\nUpgrade-Insecure-Requests: 1\n\
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3\n\
Purpose: prefetch\n\
Accept-Encoding: gzip, deflate, br\n\
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8'#How to use 
request_head=request_head_1+filename+request_head_2

clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort)) #creat connection

clientSocket.send(request_head.encode()) #encoding the message to binary bytes
for i in range(2):
    mod=clientSocket.recv(1024)
    print(mod.decode())
clientSocket.close()