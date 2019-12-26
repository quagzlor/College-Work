import socket

socko = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 3125
localhost = '127.0.0.1'

print ("Enter the number for z")
z = int(input())

socko.connect((localhost,port))

socko.send(bytes(str(z),'utf8'))

w = socko.recv(1024)
w = int(str(w,'utf8'))
print ("Value of w is: ", w)

print ("Enter y1")
y1 = int(input())

print ("Enter y2")
y2 = int(input())

socko.send(bytes(str(y1),'utf8'))
socko.send(bytes(str(y2),'utf8'))

message = socko.recv(1024)
message = str(message,'utf8')

print (message)

socko.close()