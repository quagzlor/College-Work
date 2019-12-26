import char_sender as send
import char_receiver as receive
import sys,os

#send
data = open('input.txt','r').readlines()
data = str(data)

data,flag=send.char_slice_stuff(data)

print (data)
encoded_send=[]
for i in range(0,len(data)):
    encoded_send.append(send.text_to_bits(data[i]))
send.file_write(encoded_send)

#receive
transmit_file=open('transmit.txt','r')
read_data=transmit_file.read().splitlines()

decoded_receive= receive.char_unstuff_unslice(read_data,flag)

print (decoded_receive)
