#! usr/bin/python
# -*- coding:utf-8 -*-

import socket

maxRecvSize = 1024

address = (socket.gethostname(), 6789)

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
	serverSocket.bind(address)
	print u"等待接收数据..."

	clientData, clientAddress = serverSocket.recvfrom(maxRecvSize)

	print u"接收到客户端", clientAddress, u"数据:", clientData

	serverSocket.sendto(clientData.upper(), clientAddress)

except Exception as e:
	print u"异常：", e

finally:
	serverSocket.close()
