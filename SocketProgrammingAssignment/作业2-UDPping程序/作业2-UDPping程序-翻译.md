# 套接字编程作业2：UDPping程序

**官方英文文档：[Socket2_UDPpinger.pdf](Socket2_UDPpinger.pdf)**

**以下内容为笔者翻译：**

***

## 套接字编程作业2：UDP ping 程序

在本实验中，您将学习使用Python进行UDP套接字编程的基础知识。您将学习如何使用UDP套接字发送和接收数据报，以及如何设置适当的套接字超时。在实验中，您将熟悉Ping应用程序及其在计算统计信息（如丢包率）中的作用。

您首先需要研究一个用Python编写的简单的ping服务器程序，并实现对应的客户端程序。这些程序提供的功能类似于现代操作系统中可用的标准ping程序功能。然而，我们的程序使用更简单的UDP协议，而不是标准互联网控制消息协议（ICMP）来进行通信。 ping协议允许客户端机器发送一个数据包到远程机器，并使远程机器将数据包返回到客户（称为回显）的操作。另外，ping协议允许主机计算它到其他机器的往返时间。

以下是Ping服务器程序的完整代码。你的任务是写出Ping客户端程序。

### 服务器代码

以下代码完整实现了一个ping服务器。您需要在运行客户端程序之前编译并运行此代码。*而且您不需要修改此代码。*

在这个服务器代码中，30％的客户端的数据包会被模拟丢失。你应该仔细研究这个代码，它将帮助你编写ping客户端。

``` python
# UDPPingerServer.py 
# We will need the following module to generate randomized lost packets import random 
from socket import * 

# Create a UDP socket  
# Notice the use of SOCK_DGRAM for UDP packets 
serverSocket = socket(AF_INET, SOCK_DGRAM) 
# Assign IP address and port number to socket 
serverSocket.bind(('', 12000)) 

while True:     
	# Generate random number in the range of 0 to 10 
	rand = random.randint(0, 10)     
	# Receive the client packet along with the address it is coming from  
	message, address = serverSocket.recvfrom(1024) 
	# Capitalize the message from the client     
	message = message.upper() 
	# If rand is less is than 4, we consider the packet lost and do not respond     
	if rand < 4:         
		continue     
	# Otherwise, the server responds         
	serverSocket.sendto(message, address) 
```

服务器程序在一个无限循环中监听到来的UDP数据包。当数据包到达时，如果生成一个随机整数大于或等于4，则服务器将数字转为大写并将其发送回客户端。

### 数据包丢失

UDP为应用程序提供了不可靠的传输服务。消息可能因为路由器队列溢出，硬件错误或其他原因，而在网络中丢失。但由于在内网中很丢包甚至不丢包，所以在本实验室的服务器程序添加人为损失来模拟网络丢包的影响。服务器创建一个随机整数，由它确定传入的数据包是否丢失。

### 客户端代码

您需要实现以下客户端程序。

客户端向服务器发送10次ping。因为UDP是不可靠的协议，所以从客户端发送到服务器的数据包可能在网络中丢失。因此，客户端不能无限期地等待ping消息的回复。客户等待服务器回答的时间至多为一秒，如果在一秒内没有收到回复，您的客户端程序应该假定数据包在网络传输期间丢失。您需要查找Python文档，以了解如何在数据报套接字上设置超时值。

具体来说，您的客户端程序应该

1. 使用UDP发送ping消息（注意：不同于TCP，您不需要首先建立连接，因为UDP是无连接协议。）
2. 从服务器输出响应消息
3. 如果从服务器受到响应，则计算并输出每个数据包的往返时延（RTT）（以秒为单位），
4. 否则输出“请求超时”

在开发过程中，您应该先在计算机上运行`UDPPingerServer.py`，并通过向`localhost`（或127.0.0.1）发送数据包来测试客户端。调试完成代码后，您应该能看到ping服务器和ping客户端在不同机器上通过网络进行通信。

### 消息格式

本实验中的ping消息格式使用最简单的方式。客户端消息只有一行，由以下格式的ASCII字符组成：

> Ping *sequence_number time*

其中*sequence_number*从1开始，一直到10，共10条消息，而*time*则是客户端发送消息时的时间。

### 需要上交的内容

您需要上交完整的客户端代码和屏幕截图，以验证您的ping程序是否按需求运行。

### 可选练习

1. 目前，程序计算每个数据包的往返时间（RTT），并单独打印出来。请按照标准ping程序的模式修改。您需要在客户端每次ping后显示最小，最大和平均RTT。另外，还需计算丢包率（百分比）。
2. UDP Ping的另一个类似的应用是UDP Heartbeat。心跳可用于检查应用程序是否已启动并运行，并报告单向丢包。客户端在UDP数据包中将一个序列号和当前时间戳发送给正在监听客户端心跳的服务器。服务器收到数据包后，计算时差，报告丢包（若发生）。如果心跳数据包在指定的一段时间内丢失，我们可以假设客户端应用程序已经停止。实现UDP Heartbeat（客户端和服务器端）。您需要修改给定的UDPPingerServer.py和您自己的UDP ping客户端。