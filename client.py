#Mehul Jain 1001229017
from socket import *
from time import *
import sys


HOST=sys.argv[1]
PORT=sys.argv[2]
fileName=sys.argv[3]

clientSocket = socket(AF_INET, SOCK_STREAM)

print'Client Created'


print 'Host', HOST
print 'Port', PORT


clientSocket.connect((HOST,int(PORT)))

print 'Server Address', HOST,int(PORT)

# connect the host and port to the socket

sendTime=time();

print 'File Sent To the Server', fileName
clientSocket.send(fileName)

data=clientSocket.recv(5120)

print'Data Received By the Client is', data
recTime=time()

print 'RTT', recTime-sendTime

clientSocket.close()