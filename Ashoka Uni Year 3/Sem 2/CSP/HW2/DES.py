import textwrap

SBOX = [
# Box-1
[
[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
],
# Box-2

[
[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
],

# Box-3

[
[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]

],

# Box-4
[
[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]
],

# Box-5
[
[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
],
# Box-6

[
[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]

],
# Box-7
[
[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
],
# Box-8

[
[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
]

]

P_TABLE = [16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25]

def Encryption(): #Main method for encryption
    plaintext = read_file("plaintext.txt")
    key = read_file("key.txt")

    print ("Enter the initialization vector for CBC")
    init_vect = input()

    init_vect = a2b(init_vect)
    key = a2b(key)
    plaintext = pkcs5_pad(plaintext)
    plaintext = eight_byte_split(plaintext)

    keys = subkeys(key)

    ciphered = []

    for i in range(0,len(plaintext),1):
        plain_block = a2b(plaintext[i])
        
        block = xor(init_vect,plain_block)
        
        block = feisel_net(block,keys)

        init_vect = block

        ciphered.append(block)

    write_file(ciphered,"encrypted.txt")

def Decryption(): #Main method for decryption
    ciphertext = read_file("encrypted.txt")
    key = read_file("key.txt")

    print ("Enter the initialization vector for CBC")
    init_vect = input()

    key = a2b(key)
    init_vect = a2b(init_vect)

    keys = subkeys(key)
    keys = list(reversed(keys))

    ciphertext = cipher_split(ciphertext)

    plaintext = []

    for i in range(0,len(ciphertext)):
        cipherblock = ciphertext[i]

        block = feisel_net(cipherblock,keys)

        block = xor(block,init_vect)

        init_vect = ciphertext[i]

        plaintext.append(block)
    for i in range(len(plaintext)):
        temp = int(plaintext[i],2)
        plaintext[i] = temp.to_bytes((temp.bit_length() + 7) // 8, 'big').decode()

    cipher_blocks = len(plaintext)
    plaintext[cipher_blocks-1] = remove_pad(plaintext[cipher_blocks-1]) 
    write_file(plaintext,"decrypted.txt")
    
def cipher_split(text): #Splits the cipher text into 64 bit blocks
    split_arr = [text[i:i+64] for i in range(0,len(text),64)]

    return split_arr

def eight_byte_split(text): #Splits the message into text blocks
    split_arr = [text[i:i+8] for i in range(0,len(text),8)]

    return split_arr

def six_bit_split(to_split): #Splits passed string into sets of 6 bits
    list_of_bits = textwrap.wrap(to_split,6)

    return list_of_bits

def four_bit_split(to_split): #Splits passed string into sets of 6 bits
    list_of_bits = textwrap.wrap(to_split,4)

    return list_of_bits

def pkcs5_pad(text): #Pads text using PKCS#5
    remainder = len(text) % 8
    remainder = 8 - remainder
    if remainder>0:
        for i in range(0,remainder):
            text = text+ str(remainder)

    return text

def remove_pad(text): #Removes padding from text
    lastnum = text[7]
    if lastnum.isdigit():
        unpadded = text[:(8-int(lastnum))]
    text = unpadded

    return text

def s_box_lookup(bits,boxnumber): #Takes 6 bits, and returns the s_box
    row = bits[0] + bits[5]
    row = int(row,2)
    
    column = bits[1:5]
    column = int(column,2)

    sbox_val = SBOX[boxnumber][row][column]
    sbox_val = bin(sbox_val)
    sbox_val = sbox_val[2:]

    if len(sbox_val)<4:
        for i in range(4-len(sbox_val)):
            sbox_val = '0' + sbox_val
    return sbox_val

def feisel_net(text,subkeys): #Performs the 16 rounds of the DES

    L_arr = text[:32]
    R_arr = text[32:]

    for i in range(0,16,1):
        L_arr = xor(L_arr,feisel_func(R_arr,subkeys[i]))

        temp = R_arr
        R_arr = L_arr
        L_arr = temp
    temp = R_arr
    R_arr = L_arr
    L_arr = temp

    block = L_arr + R_arr

    return block

def feisel_func(block,subkey): #Performs the fiestel function
    block = four_bit_split(block)
    six_bit_arr = []
    four_bit_arr = []

    # Expansion Step
    for i in range(0,8,1):
        previous_piece = block[i-1]
        next_piece = block[(i+1)%8]
        six_bit_arr.append(previous_piece[3:] + block[i] + next_piece[:1])

    # Key mixing
    block = ""

    for i in range(0,len(six_bit_arr)):
        block = block + six_bit_arr[i]

    block = xor(block,subkey)

    #Substitution
    block = six_bit_split(block)

    for i in range(0,len(block)):
        four_bit_arr.append(s_box_lookup(block[i],i))

    #Permutation
    block = ""
    for i in range(0,len(four_bit_arr)):
        block = block + four_bit_arr[i]

    final_block = ""

    for i in range(0,32):
        final_block = final_block + block[P_TABLE[i]-1]

    return final_block

def subkeys(init_key): #Generates the subkeys from a master key
    subkeys = []
    for i in range(16):
        subkey = init_key[:24] + init_key[:-24]
        subkeys.append(subkey)
        init_key = init_key[16:] + init_key[:16]

    return subkeys

def a2b(text): #Converts ascii to binary
    text = str(text)
    info = bin(int.from_bytes(text.encode(), 'big'))

    info = info[0] + info[2:]
    return info

def xor(a,b): #XOR function, easier than using python's built in
    xor_ed = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            xor_ed = xor_ed + '0'
        else:
            xor_ed = xor_ed + "1"
    return xor_ed

def read_file(filename): #Reads the passed file
    file_read = open(filename,"r")
    info = file_read.read()
    file_read.close()
    
    return info

def write_file(info, filename): #Writes the passed data
    file_write = open(filename,"w")
    file_write.writelines(info)
    file_write.close()

def main(): #Main control
    print ("Enter 1 for encrypt, 2 for decrypt")
    choice = int(input())
    if choice == 1:
        Encryption()
    elif choice == 2:
        Decryption()
    else:
        print ("Try again")
main()