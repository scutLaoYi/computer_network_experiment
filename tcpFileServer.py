#usr/bin/python
# -*- coding:utf-8 -*-

import socket

serverSocket = socket.socket()

host = socket.gethostname()
port = 6789
maxListenLength = 10


try:
	fileLoc = raw_input("输入要发送的文件路径:")

	filePtr = open(fileLoc)

	serverSocket.bind((host, port))
	serverSocket.listen(maxListenLength)
	print u"文件已打开，监听端口6789..."

	client, address = serverSocket.accept()
	print u"接收到来自", address, u"的连接，开始发送数据..."

	for line in filePtr:
		client.send(line)
	
	print u"文件传送成功！服务器退出..."
	client.close()

except IOError as e:
	print u"文件打开失败...", e

except EnvironmentError as e:
	print u"绑定socket失败...", e

except KeyboardInterrupt:
	serverSocket.close()
	print u"按键退出，服务器退出..."

finally:
	serverSocket.close()
	filePtr.close()


