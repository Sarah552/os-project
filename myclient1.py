
import socket               # Import socket module
from thread import *

s = socket.socket()         
host = socket.gethostname()
port = 5188                # Reserve a port for your service.
s.connect((host, port))

def clientthread(s):
    while 1:
	print s.recv(1024)	

start_new_thread(clientthread ,(s,))			
while(1):
	data= raw_input('')
	s.sendall(data) 
	if str(data) == 'exit':
		s.close                     # Close the socket when done
