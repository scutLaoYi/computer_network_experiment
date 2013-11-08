#!user/bin/python
# -*- coding:utf-8 -*-

import socket

clientSocket = socket.socket()

host = socket.gethostname()
port = 6789
maxRecieveSize = 1024

try:
	clientSocket.connect((host, port))
	print u"连接创建成功！"
	message = raw_input(u"message:")
	clientSocket.send(message)
	
	serverMessage = clientSocket.recv(maxRecieveSize)
	print u"服务器返回数据：", serverMessage

except Exception as e:
	print "Exception occur:", e



