import socket
TCP_IP = '127.0.0.1'
TCP_PORT = 2345
BUFFER_SIZE = 8192

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
data = s.recv(BUFFER_SIZE)

#jisir = input("Enter 1 to add files, 2 to get files:")

#if jisir = 1:

#if jisir = 2:
 #   implement getfiles here
#if jisir != 1 and jisir != 2:
 #   print "wtf"


#def getfiles():
moreQuery='y'
while moreQuery=='y' or moreQuery=='Y':
    formatList=data.split(',')

    for i in range(0, len(formatList)):
        print str(i+1)+'. '+formatList[i]
    k=input("Please enter the integer corresponding to your format: ")
    while k<1 or k>=(len(formatList)+1):
        print "Invalid format number. Please choose a number from the above list and try again."
        k=input("Please enter the integer corresponding to your format: ")
    print "\nThe Files correponding to format " + formatList[k-1]+ " are "

    s.send(str(k-1))
    results=s.recv(BUFFER_SIZE)

    result = results.split(',')

    for i in range (0,len(result)):
        print (str(i)+")"+result[i])

    h = input("Please enter the file name of the file you want without the extension: ")
    #s.send(h)

    #f = open(h+'.'+formatList(k-1),'wb') #enter user's extension
    #x = s.recv(8192000)
    #f.write(x)



    moreQuery=raw_input("\nDo you want to perform more queries ? Y/N ")
s.close()
