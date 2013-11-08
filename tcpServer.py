#!usr/bin/python
# -*- coding:utf-8 -*-

import socket

serverSocket = socket.socket()

host = socket.gethostname()
port = 6789
maxListenLength = 10
maxRecieveSize = 1024

try:
	serverSocket.bind((host, port))
	
	serverSocket.listen(maxListenLength)
	print u'开始监听端口6789...'

	while True:
		try:
			client, address = serverSocket.accept()
			print u"接收到来自", address, u"的连接"
			messageFromClient = client.recv(maxRecieveSize)
			print u"客户端发送数据：", messageFromClient
			client.send(messageFromClient.upper())

		except Exception as e:
			print u"出现一个异常"
			print e

		finally:
			client.close()


except EnvironmentError as e:
	print u"绑定socket失败..."
	print e
