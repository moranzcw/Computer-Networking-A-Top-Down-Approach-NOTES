from socket import *
PORT=800
serverSocket = socket(AF_INET, SOCK_STREAM) 
serverSocket.bind(('', PORT)) # 将TCP欢迎套接字绑定到指定端口
serverSocket.listen(1) # 最大连接数为1

while True:
	print('Ready to serve...')
	connectionSocket, addr = serverSocket.accept() # 接收到客户连接请求后，建立新的TCP连接套接字
	try:
		message = connectionSocket.recv(1024) # 获取客户发送的报文
		filename = message.split()[1]
		print(message)#######################
		if filename=='/':
			raise IOError
		f = open(filename[1:])
		outputdata = f.read()
		#Send one HTTP header line into socket
		header = ' HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html\nContent-Length: %d\n\n' % (len(outputdata))
		connectionSocket.send(header.encode())

		#Send the content of the requested file to the client
		'''
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i].encode())
		'''
		connectionSocket.send(outputdata.encode())
		#两种发送方法都可，显然上一种速度更慢
		connectionSocket.close()
	except IOError:
		#Send response message for file not found
		header = ' HTTP/1.1 404 Not Found'
		connectionSocket.send(header.encode())
		
		#Close client socket
		connectionSocket.close()
serverSocket.close()