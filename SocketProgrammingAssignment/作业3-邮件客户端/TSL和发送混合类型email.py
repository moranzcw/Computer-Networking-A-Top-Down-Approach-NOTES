
from socket import *
import base64
endmsg = ".\r\n"

mail_t='1254516725@qq.com'


#chose qq mail smtp server
mailserver = 'smtp.qq.com'
fromaddr='2634081011@qq.com'
toaddr='galliumwang@163.com'
user='MjYzNDA4MTAxMUBxcS5jb20='
passw='aXFvcm1ncGd2aHp2ZWNnaQ=='
serverPort=25
serverPort_TLS=587
clientSocket = socket(AF_INET, SOCK_STREAM) 
clientSocket.connect((mailserver, serverPort))#根据需求选择是否需要TLS加密的端口


recv = clientSocket.recv(1024).decode()
print(recv)

# Send HELO command and print server response.
heloCommand = 'HELO 169.254.186.23\r\n'
print(heloCommand)
clientSocket.send(heloCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)

'''
temp='STARTTLS\r\n'
print(temp)
clientSocket.send(temp.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
'''#如果选择TLS加密则去除该段注释符

# Send MAIL FROM command and print server response.
# Fill in start
temp='AUTH login\r\n'
print(temp)
clientSocket.send(temp.encode())
recv = clientSocket.recv(1024).decode()
print(recv)

temp=user+'\r\n'
print(temp)
clientSocket.send(temp.encode())
recv = clientSocket.recv(1024).decode()
print(recv)

temp=passw+'\r\n'
print(temp)
clientSocket.send(temp.encode())
recv = clientSocket.recv(1024).decode()
print(recv)

temp='mail from:<'+fromaddr+'>\r\n'#########
print(temp)
clientSocket.send(temp.encode())
recv = clientSocket.recv(1024).decode()
print(recv)

# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
temp='rcpt to:<'+toaddr+'>\r\n'
print(temp)
clientSocket.send(temp.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
# Fill in end


# Send DATA command and print server response.
# Fill in start
temp='data\r\n'
print(temp)
clientSocket.send(temp.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
# Fill in end


#此部分可伪造收件人和发件人/除最后一处外，其余地方 \r\n or \n 皆可


send_text='from:%s\nto:%s\nsubject:hello,you!\
\nContent-Type:text/plain\n'%(fromaddr,toaddr)+'\n'+'hello'+'\r\n'
send_text=send_text.encode()

send_html='from:%s\nto:%s\nsubject:hello,you!\
\nContent-Type:text/html\n'%(fromaddr,toaddr)+'\n'+'<h1>hello</h1><img src="https://pic3.zhimg.com/50/v2-29a01fdecc80b16e73160c40637a5e8c_hd.jpg">'+'\r\n'
send_html=send_html.encode()

f=open('gfriend.jpg','rb').read()
f=base64.b64encode(f) 
send_image=('from:%s\nto:%s\nsubject:hello,you!\
\nContent-Type:image/JPEG\nContent-transfer-encoding:base64\n'%(fromaddr,toaddr)+'\n').encode()+f+'\r\n'.encode() 
#需要指定图片的编码类型

send_text_with_image='from:%s\nto:%s\nsubject:hello,you!\
\nContent-Type:multipart/mixed;boundary="simple"\n\n--simple\n'%(fromaddr,toaddr)+'Content-Type:text/html\n\n<h1>hello</h1><img src="https://pic3.zhimg.com/50/v2-29a01fdecc80b16e73160c40637a5e8c_hd.jpg">\n\n'
send_text_with_image=send_text_with_image.encode()+'--simple\n'.encode()+'Content-Type:image/JPEG\nContent-transfer-encoding:base64\n\n'.encode()
f=open('gfriend.jpg','rb').read()
f=base64.b64encode(f) 
send_text_with_image+=f
send_text_with_image+='\n--simple\r\n'.encode()

temp=send_text_with_image
print(temp)
clientSocket.send(temp)


temp=endmsg
print(temp)
clientSocket.send(temp.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
# Fill in end

# Send QUIT command and get server response.
# Fill in start
temp='quit\r\n'
print(temp)
clientSocket.send(temp.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
# Fill in end
 