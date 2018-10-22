# Mehul Jain 1001229017
from socket import *
from time import  *
import sys
from thread import *

HOST='127.0.0.1'
PORT=8011
serverSocket = socket(AF_INET, SOCK_STREAM)

print 'Socket Created'
serverSocket.bind((HOST, PORT)) # bind the host and port to the socket
serverSocket.listen(1) # start listening

print 'Server Port', PORT
print 'Host:',HOST


def clientThread(connectionSocket):

 #Establish the connection
    print 'Ready to Serve...'
    try:
        message = connectionSocket.recv(5120).decode('utf-8')

        f = open(message,'rb') # open file with read and byte permissions
        outputdata = f.read()
        f.close() #close the file after taking the data

        header = 'HTTP/1.1 200 OK\n'

    except Exception as e: # handle exceptions
        header = 'HTTP/1.1 404 Not Found\n\n' #if file not found
        outputdata = '<html><body><center><h3>Error 404: File not found</h3><p>Python HTTP Server</p></center></body></html>'.encode('utf-8')
        print("File not Found")

    final_response = header.encode('utf-8')
    final_response += outputdata

    connectionSocket.send(final_response)  #send the data to the socket
    connectionSocket.send(final_response) # send the final response
    connectionSocket.close() # close the connection


while True:  #multi-threading

    print 'Ready to Serve'

    conn,threadAddr=serverSocket.accept()

    print 'Thread No.:', threadAddr[1]

    # function call to execute multithreading
    start_new_thread(clientThread,(conn,))
