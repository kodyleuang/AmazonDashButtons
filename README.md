# ChatServer
This is the python chat server script that is run on our raspberry pi.  It allows users to send messages to all other devices
in the chat room.  Note: My router is set up to assign the IP address of 10.0.1.10 to the raspberry pi.  The port is set up in the script (in this case, it is set to 5000).  To join the chat room from a computer, open a terminal window and do the following:

First, start python

Then, import socket:   >>>import socket

Create a socket:       >>>s = socket.socket()

Make the connection:   >>>s.connect(("10.0.1.10", 5000))

The command to send a message depends on if you are in python 2.7 or python 3.X:

python 2.7:    >>>s.sendall("Put your message here")

python 3.X:    >>>s.sendall(b"Put your message here")

To receive messages:    >>>s.recv(4048)

To close the socket:    >>>s.close()
