'''
    Simple socket server using threads
'''

import socket
import sys
from thread import *
list=[]
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 5188 # Arbitrary non-privileged port


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

#Function for handling connections. This will be used to create threads
def clientthread(c1,i):
    #Sending message to connected client
    c1.send('Welcome to the server.') #send only takes string

    #infinite loop so that function do not terminate and thread do not end.

    while True:

        #Receiving from client
        data = c1.recv(1024)
        if i==0:
            c1=list[1]
            c1.send(data)
            c1=list[0]
        elif i == 1:
            c1 = list[0]
            c1.send(data)
            c1 = list[1]

    c1.close()

#now keep talking with the client
i=0

while 1:
    #wait to accept a connection - blocking call
     conn, addr = s.accept()
     print 'Connected with ' + addr[0] + ':' + str(addr[1])
     list.append(conn)
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
     start_new_thread(clientthread ,(conn,i))
     i=i+1
s.close()
