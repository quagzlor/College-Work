import socket
TCP_IP = '127.0.0.1'
TCP_PORT = 2345
BUFFER_SIZE = 8192  # Normally 1024, but we want fast response
f=open('Logs.txt','r')
t=f.read()
f.close()
t=t.split('\n')
n=len(t)/3
files={}
dnn={}
formats={}
#print files
for i in range(0,n):
    files[i]=t[i*3]
    formats[i]=t[(i*3)+1]
    dnn[i]=t[(i*3)+2]

formatrev={}
for i in range(0,n):
    for j in range(0, len(dnn[i])):
        if dnn[i][j] not in formatrev:
            formatrev[dnn[i][j]]=[]
        if i not in formatrev[dnn[i][j]]:
            formatrev[dnn[i][j]].append(i)

extensionnos = []
for each in formatrev.values():
	extensionnos.append(each[0])

extensions = []
formatabc = formats.values()

for i in range(0,len(extensionnos)/3):
	for i in extensionnos:
		extensions.append(formatabc[i])

data = ','.join(extensions)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
conn.send(data)

formatrevabc = formatrev.values()
filesabc = files.values()

print "Server is up :)"

while 1:

	format_data=conn.recv(BUFFER_SIZE)
	if not format_data: break
	resultList=[]
	for each in formatrevabc[int(format_data)]:
		resultList.append(files[each]+'.'+formatabc[each])
	conn.send(str(resultList))

#h = conn.recv(BUFFER_SIZE)

#g = conn.send(h)

conn.close()
