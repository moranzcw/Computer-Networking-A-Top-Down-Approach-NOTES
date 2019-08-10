from socket import * 
import random
import time
serverSocket = socket(AF_INET, SOCK_DGRAM) 
serverPort=800
serverSocket.bind(('',serverPort)) 


start_time=float(time.time())
end_time=start_time

while True:     
	
	try:
		serverSocket.settimeout(0.1)
		message, address = serverSocket.recvfrom(1024)
		message=message.decode()
		rtime=float(message.split()[1])
		end_time=rtime
		Ping=float(time.time())-rtime
		print(str(message.split()[0])+':',Ping)
	except Exception as e:
		if end_time==start_time:
			continue
		if time.time()-end_time>=1.0:
			print('Heartbeat pause')
			break
		else:
			print('Packet lost')
	'''
	1: 0.0010023117065429688
	2: 0.0009434223175048828
	3: 0.0009434223175048828
	4: 0.0029366016387939453
	5: 0.0029366016387939453
	6: 0.004778385162353516
	7: 0.004778385162353516
	8: 0.00577998161315918
	9: 0.00577998161315918
	10: 0.006776571273803711
	Packet lost
	Packet lost
	Packet lost
	Packet lost
	Packet lost
	Packet lost
	Packet lost
	Packet lost
	Packet lost
	Heartbeat pause
	'''