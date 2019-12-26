import binascii
import sys, os

def file_write(to_write):
    write_file=open("transmit.txt","w")

    write_file.write("")

    write_file.close()

    write_file=open("transmit.txt","a")
    
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

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits=[]
    for i in range(0,len(text)):
        bits.append(bin(int(binascii.hexlify(text[i].encode(encoding, errors)), 16))[2:])

        for i in range(0,len(bits)):
            bits[i].zfill(8 * ((len(bits) + 7) // 8))

    return bits
