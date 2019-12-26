import binascii
import sys, os

def main():
    file_read_data=file_read()

    char_slice_stuff_data=char_slice_stuff(file_read_data)

    crc_32_data=crc_32_convert(char_slice_stuff_data)

    file_write(crc_32_data)
    
def file_read():
    file_read=open("F.txt","r")

    text_to_send= file_read.read()

    file_read.close()

    return text_to_send

def file_write(to_write):
    write_file=open("f_send.txt","w")

    write_file.write("")

    write_file.close()

    write_file=open("f_send.txt","a")
    
    for i in range(0,len(to_write)):
        write_file.write(str(to_write[i]))
        write_file.write('\n')

    write_file.close()

def char_slice_stuff(text):
    slice_text=[]

    print ("Enter the flag")
    flag=input()

    text=text[2:(len(text)-2)]

    for i in range(0,len(text),8):
        slice_text.append(text[i:(i+8)])

    for i in range(0,len(slice_text)):
        slice_text[i]=flag+"STX"+slice_text[i].replace(flag,flag+flag)+"ETX"+flag

    return slice_text,flag

def crc_32_convert(string_array):
    crc_array=[]

    for i in range(len(string_array)):
        to_encode=str(string_array[i])
        crc_mod = int(binascii.crc32(to_encode.encode()))
        crc_array.append(bin(crc_mod))

    return crc_array
