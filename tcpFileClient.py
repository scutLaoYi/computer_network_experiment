#!usr/bin/python
# -*- coding:utf-8 -*-

import socket

clientSocket = socket.socket()

host = socket.gethostname()
port = 6789

try:
	clientSocket.connect((host, port))
	print u"服务器连接成功！接收数据..."
	fileLoc = raw_input('输入保存的文件名:')

	filePtr = open(fileLoc, 'w')

	data = clientSocket.recv(65535)

	filePtr.write(data)
	print u"数据接收完成.客户端退出."
	
finally:
	filePtr.close()
	clientSocket.close()
