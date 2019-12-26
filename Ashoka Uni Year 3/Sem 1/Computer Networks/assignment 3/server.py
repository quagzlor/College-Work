import socket
import random
from scapy.all import *
from contextlib import redirect_stdout as redirect
import io
import subprocess
import threading

def server():

    if (z == y1*y2):
        if (w == lsd1 or w == lsd2):
            client.send(bytes(str('You Win'),'utf8'))
        else:
            client.send(bytes(str('You Lost'),'utf8'))
    else:
        print ("z is not equal to y1 x y2")

    client.close()
    socko.close()

def TCPDump():
    stinky = sniff(count = 20,filter = "\host 127.0.0.1 port %s and tcp" % address[1])
    print ("sniffer done")

    output_file = io.StringIO()
    with redirect(output_file):
        stinky[-2].show()

    write_file = open("packet.txt","w")
    write_file.write(output_file.getvalue())
    write_file.close()

socko = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 3125
localhost = '127.0.0.1'

coin_toss = ['3','5']
w = random.sample(coin_toss,1)
w = int(w[0])


socko.bind((localhost,port))

print ("Socket is listening on port 3125")
socko.listen(5)

(client,address) = socko.accept()
print ("Connected to: ", address)

#receives z, and send w
z = client.recv(1024)
print (str(z,'utf8'))
client.send(bytes(str(w),'utf8'))

y1 = client.recv(1024)
y2 = client.recv(1024)

z = int(str(z,'utf8'))
y1 = str(y1,'utf8')
y2 = str(y2,'utf8')

lsd1 = int(y1[-1:])
lsd2 = int(y2[-1:])

y1 = int(y1)
y2 = int(y2)

dump_thread = threading.Thread(target = TCPDump, args = [])
server_thread = threading.Thread(target = server, args = [])

package_to_send = []
dump_thread.start()
server_thread.start()