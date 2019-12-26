import socket
TCP_IP = '127.0.0.1'
TCP_PORT = 2345
BUFFER_SIZE = 8192000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

data = s.recv(1024)

f = open(data+".mp4",'rb')
print "Sending"
g = f.read(BUFFER_SIZE)

while(g):
	print 'Sending...'
    s.send(g)
    g = f.read(BUFFER_SIZE)

f.close()
print "Done :)"
s.send()
