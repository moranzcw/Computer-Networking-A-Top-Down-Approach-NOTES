from socket import *
import sys
import _thread

name='localhost'
port=2000

def main():
	try:
		serverSocket=socket(AF_INET,SOCK_STREAM)
		serverSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
		serverSocket.bind((name,port))
		serverSocket.listen(50)
	except (error,msg):
		if serverSocket:
			serverSocket.close()
		print("socket error"),
		print(msg)
		sys.exit(1)
	while 1:
		connectionSocket,address=serverSocket.accept()
		_thread.start_new_thread(webproxy,(connectionSocket,address))
	serverSocket.close()

def webproxy(connectionSocket,address):
	request=connectionSocket.recv(1024).decode()
	start=request.find('/')
	end=request.find('HTTP')
	
	servername=request[start+1:end]
	request=request[:start+1]+" "+request[end:]	
	start=request.find('Host')
	start=request.find(":",start)
	end=request.find("\n",start)
	request=request[:start+1]+" "+servername.rstrip()+":"+"80"+request[end:]
	print(request)
	

	clientSocket=socket(AF_INET,SOCK_STREAM)
	print(servername)
	try:
		clientSocket.connect((servername,80))
		clientSocket.send(request)

		response=clientSocket.recv(1024)
		print(response)
		connectionSocket.send(response)
		clientSocket.close()
		connectionSocket.close()
	except (error,msg):
		if clientSocket:
			clientSocket.close()
		if connectionSocket:
			connectionSocket.close()
		print(msg)
		sys.exit(1)

if __name__== '__main__':
	main()
