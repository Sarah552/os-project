'''
    Simple socket server using threads
'''
 
import socket
import sys
from thread import *
 
HOST = ''   # Symbolic name1e meaning all available interfaces
PORT = 5188# Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#Start listening on socket
s.listen(10)
print 'Socket now listening'
def Display(cuser):
	loop1 = len(arr)
	while loop1:
		loop1 -= 1
		arr[loop1]['con'].send("\n" + cuser['name1'] + " is recently Connected")
	return
#Function for handling connections. This will be used to create threads
def clientthread(conn):
	while 1:
		data = conn.recv(1024)
		if conn == arr[0]['con']:
			conn = arr[1]['con']
			conn.send(data)
			conn = arr[0]['con']
		elif conn == arr[1]['con']:
			conn = arr[0]['con']
			conn.send(data)
			conn = arr[1]['con']
	conn.close()
def DisplayUsers(conn):
	conn.send("Connected User are: \n")
	loop1 = len(arr)
	while loop1:
		loop1 -= 1
		conn.send(arr[loop1]['name1']+"\n")
	return
arr =[]
i = 0
while 1:
    conn, addr = s.accept()
    cuser = {}
    cuser['con'] = conn
    cuser['addr1'] = addr
    cuser['name1'] = conn.recv(200)
    Display(cuser)
    arr += [cuser]
    DisplayUsers(conn)
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
     
    #start new thread takes 1st argument as a function name1e to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))
    i += 1
 
s.close()

