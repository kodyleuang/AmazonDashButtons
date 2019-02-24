#this is the script that listens for network traffic involving the specific 
#Amazon Dash buttons with the indicated MAC addresses and sends a message through
#the python chat server

#based on aaron bell's project (using sockets instead of scapy for monitoring 
#network traffic:
#http://www.aaronbell.com/how-to-hack-amazons-wifi-button/

import struct
import binascii
import socket

#creating a dictionary with the MAC addresses of the Dash buttons and the
#message sent on the chat server as key:value pairs
macs = {
    '7475483bfbd2' : 'maxwell',
    '10ae60fa281c' : 'mac_cheese',
    'a002dc968e5c' : 'elements',
    '6837e9828f7b' : 'emergency',
    '74c246e0926d' : 'gatorade',
    '6837e90c4dd2' : 'poof',
    'fca667794a5e' : 'sky',
    '74c246c46424' : 'cottonelle',
    'fca667d30173' : 'quest',
    'f0272d7a0cd7' : 'kitty'
}

rawSocket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))


while True:
    packet = rawSocket.recvfrom(2048)
    ethernet_header = packet[0][0:14]
    ethernet_detailed = struct.unpack("!6s6s2s", ethernet_header)
    
    arp_header = packet[0][14:42]
    arp_detailed = struct.unpack("2s2s1s1s2s6s4s6s4s", arp_header)

    # skip non-ARP packets
    ethertype = ethernet_detailed[2]

    if ethertype != '\x08\x06':
        continue
    # read out data
    source_mac = binascii.hexlify(arp_detailed[5])
    dest_ip = socket.inet_ntoa(arp_detailed[6])

    #diagnostic print statement
    #print "Source MAC = " + source_mac

    if source_mac in macs:
        message = macs[source_mac]
	
	#encode the message for Python 3.X
	byteMessage = message.encode('utf-8')
	
	#diagnostic print statement
        #print message + " was pressed MAC address = " + source_mac
	
	#connect to the chat server
	s = socket.socket()
	s.connect(("10.0.1.10", 5000))
        
	
	#send the message to the devices on the chat server
	s.sendall(byteMessage)
	
	#close the socket
	s.close()
    #else:
	#diagnostic print statement
        #print "unknown ping with MAC = " + source_mac + " and IP = " + dest_ip
