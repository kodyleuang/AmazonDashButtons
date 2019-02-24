#!/usr/bin/python

import socket, select

def broadcast_data(sock, message):
	for socket in CONNECTION_LIST:
		if socket != server_socket and socket != sock:
			try:
				socket.send(message)
			except:
				socket.close()
				CONNECTION_LIST.remove(socket)

if __name__ == "__main__":
	CONNECTION_LIST = []
	RECV_BUFFER = 4048
	PORT = 5000

	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind(("", PORT))
	server_socket.listen(10)
	CONNECTION_LIST.append(server_socket)
	print "Server started on port " + str(PORT)

	while 1:
		read_sockets, write_sockets, error_sockets = select.select(CONNECTION_LIST, [], [])
		for sock in read_sockets:
			if sock == server_socket:
				sockfd, addr = server_socket.accept()
				CONNECTION_LIST.append(sockfd)
			else:
				try:
					data = sock.recv(RECV_BUFFER)
					if data:
						broadcast_data(sock, data)
				except:
					pass

	server_socket.close()
