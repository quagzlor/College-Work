import binascii
import sys, os

def char_unstuff_unslice(bit_text,flag):
    end_message=""
    
    start_sequence=flag+"STX"
    end_sequence="ETX"+flag

    print (bit_text)
    for i in range(0,len(bit_text)):
        mid_text=(text_from_bits(bit_text[i]))
        print (mid_text)

        mid_text= mid_text.replace(start_sequence,"")
        mid_text= mid_text.replace(end_sequence,"")
        mid_text= mid_text.replace((flag+flag),flag)

        end_message=end_message+mid_text

    return end_message

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):

    x = bits.replace("[",'').replace("'","").replace(",","").replace("]","").replace(" ","")

    n = int(x, 2)

    return int2bytes(n).decode(encoding, errors)

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))
