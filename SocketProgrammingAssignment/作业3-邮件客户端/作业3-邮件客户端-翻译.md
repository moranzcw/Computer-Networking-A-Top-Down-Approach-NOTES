# 套接字编程作业3：邮件客户端

**官方英文文档：[Socket3_SMTP.pdf](Socket3_SMTP.pdf)**

**以下内容为笔者翻译：**

***

## 套接字编程作业3：SMTP

通过完成本实验，您将更加了解SMTP协议。您还将学到使用Python实现标准协议的经验。

您的任务是开发一个简单的邮件客户端，将邮件发送给任意收件人。您的客户端将需要连接到邮件服务器，使用SMTP协议与邮件服务器进行对话，并向邮件服务器发送电子邮件。 Python提供了一个名为smtplib的模块，它内置了使用SMTP协议发送邮件的方法。但是我们不会在本实验中使用此模块，因为它隐藏了SMTP和套接字编程的细节。

为了限制垃圾邮件，一些邮件服务器不接受来源随意的TCP连接。对于下面所述的实验，您可能需要尝试连接到您的大学邮件服务器和流行的Webmail服务器（如AOL邮件服务器）。您也可以尝试从您的家和您的大学校园进行连接。

### 代码

下面你会找到客户端的代码框架。您将完成代码框架。您需要填写代码的地方标有#Fill in start和#Fill in end。每个地方都可能需要不止一行代码。

### 附加说明

在某些情况下，接收邮件服务器可能会将您的电子邮件分类为垃圾邮件。当您查找从客户端发送的电子邮件时，请检查垃圾邮件文件夹。

### 要上交的内容

在您的上交内容中，你需要提供完整的SMTP邮件客户端的代码以及一张能显示您确实收到电子邮件的屏幕截图。

### 邮件客户端的Python代码框架

```python
from socket import *
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver 
mailserver = #Fill in start   #Fill in end
# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start

#Fill in end
recv = clientSocket.recv(1024)
print recv
if recv[:3] != '220':
    print '220 reply not received from server.'

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
    print '250 reply not received from server.'

# Send MAIL FROM command and print server response.
# Fill in start

# Fill in end

# Send RCPT TO command and print server response.
# Fill in start

# Fill in end

# Send DATA command and print server response.
# Fill in start

# Fill in end

# Send message data.
# Fill in start

# Fill in end 

# Message ends with a single period.
# Fill in start

# Fill in end

# Send QUIT command and get server response.
# Fill in start

# Fill in end
 
```

### 可选练习

1. 类似Google邮件的服务器（如地址：smtp.gmail.com，端口：587））要求您的客户端在发送MAIL FROM命令之前，需要为了身份验证和安全原因添加传输层安全（TLS）或安全套接字层（SSL）。将TLS / SSL命令添加到现有的命令中，并使用上述地址和端口为Google邮件服务器实现客户端。 
2. 您当前的SMTP邮件客户端只能在电子邮件正文中发送文本消息。修改您的客户端，使其可以发送包含文本和图像的电子邮件。