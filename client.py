
import socket               # Import socket module
import thread
s = socket.socket()         
host = socket.gethostname()
port = 5188                # Reserve a port for your service.

s.connect((host, port))
#print s.recv(1024)
print s.recv(1024)+"Enter your message for client2.\n"
def fun():
       while 1:
          srv = s.recv(1024)
          print "Client2 : "+srv
thread.start_new_thread(fun,())
while 1:
   # msg=raw_input("Enter the message for client.")
   msg = raw_input()
   s.send(msg)


# Close the socket when done
s.close()