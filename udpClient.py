#! usr/bin/python
# -*- coding:utf-8 -*-

import socket

maxRecvSize = 1024

address = (socket.gethostname(), 6789)
try:
	clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	data = raw_input("data to send:")
	clientSocket.sendto(data, address)

	recvData = clientSocket.recvfrom(maxRecvSize)
	print u"服务器", recvData[1], u"发来数据:", recvData[0]
except Exception as e:
	print u"异常：", e
finally:
	clientSocket.close()

clientSocket.close()
