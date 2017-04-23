# 编程作业1：Web服务器（中文文档）

官方给出了该作业的详细英文文档：[Socket1_WebServer.pdf](assignment/Socket1_WebServer.pdf)

以下文档内容为笔者给出的中文翻译：

> #### 套接字编程作业1：Web服务器
>
> 在本实验中，您将学习Python中TCP连接的套接字编程的基础知识：如何创建套接字，将其绑定到特定的地址和端口，以及发送和接收HTTP数据包。您还将学习一些HTTP首部格式的基础知识。
>
> 您将开发一个处理一个HTTP请求的Web服务器。您的Web服务器应该接受并解析HTTP请求，然后从服务器的文件系统获取所请求的文件，创建一个由响应文件组成的HTTP响应消息，前面是首部行，然后将响应直接发送给客户端。如果请求的文件不存在于服务器中，则服务器应该向客户端发送“404 Not Found”差错报文。
>
> ##### 代码
>
> 在文件下面你会找到Web服务器的代码骨架。您需要填写这个代码。而且需要在标有#Fill in start 和 # Fill in end的地方填写代码。另外，每个地方都可能需要不止一行代码。
>
> ##### 运行服务器
>
> 将HTML文件（例如HelloWorld.html）放在服务器所在的目录中。运行服务器程序。确认运行服务器的主机的IP地址（例如128.238.251.26）。从另一个主机，打开浏览器并提供相应的URL。例如：
>
> http://128.238.251.26:6789/HelloWorld.html
>
> “HelloWorld.html”是您放在服务器目录中的文件。还要注意使用冒号后的端口号。您需要使用服务器代码中使用的端口号来替换此端口号。在上面的例子中，我们使用了端口号6789. 浏览器应该显示HelloWorld.html的内容。如果省略“:6789”，浏览器将使用默认端口80，只有当您的服务器正在端口80监听时，才会从服务器获取网页。
>
> 然后用客户端尝试获取服务器上不存在的文件。你应该会得到一个“404 Not Found”消息。
> ##### Web服务器代码骨架
> ```python
> #import socket module
> from socket import *
> serverSocket = socket(AF_INET, SOCK_STREAM) 
> #Prepare a sever socket 
> #Fill in start 
> #Fill in end 
> while True:     
> 	#Establish the connection    
> 	print 'Ready to serve...'     
> 	connectionSocket, addr =   #Fill in start  #Fill in end
> 	try:         
> 		message =   #Fill in start  #Fill in end
> 		filename = message.split()[1]                          
> 		f = open(filename[1:])
> 		outputdata = #Fill in start  #Fill in end
> 		#Send one HTTP header line into socket         
> 		#Fill in start         
> 		#Fill in end    
> 	    
> 		#Send the content of the requested file to the client
> 		for i in range(0, len(outputdata)):
> 			connectionSocket.send(outputdata[i])
> 		connectionSocket.close()
> 	except IOError:
> 		#Send response message for file not found
> 		#Fill in start
> 		#Fill in end
> 		
> 		#Close client socket
> 		#Fill in start
> 		#Fill in end             
> serverSocket.close()
> ```

