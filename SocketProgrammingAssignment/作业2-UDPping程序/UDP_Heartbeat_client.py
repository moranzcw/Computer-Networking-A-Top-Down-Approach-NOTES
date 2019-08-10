#可选练习一较简单，故略过
from socket import *
import time
servername='127.0.0.1'
serverPort=800
clientSocket=socket(AF_INET,SOCK_DGRAM)
for i in range(1,11):
    stime=time.time()
    message=str(i)+' '+str(time.time())
    clientSocket.sendto(message.encode(),(servername,serverPort))

clientSocket.close()