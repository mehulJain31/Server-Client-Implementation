# Server-Client-Implementation
Implementation to send packets from the server to the client after the client requests a page or file on the server. 
Multi-threaded implementation in Python 2.7.

To run:
Run the server with the command: python server.py
	Server displays all the necessary connection parameters

Run the client.py with command: python2 client.py 127.0.0.1 8083 testFile.html

The output will be displayed in the client after it sends the file name to the server and then the server after opening it, sends the data back to the client.

Multi threaded implementation.

Done.
