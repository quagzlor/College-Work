from collections import deque
from operator import xor, itemgetter
import sys

sboxes = [
			[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7, 
			0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8, 
			4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0, 
			15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],

			[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
			3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5, 
			0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
			13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],

			[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8, 
			13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1, 
			13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7, 
			1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],

			[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
			13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
			10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
			3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],

			[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
			14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
			4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
			11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],

			[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
			10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
			9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
			4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],

			[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
			13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
			1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
			6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],

			[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
			1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
			7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
			2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
		]

perm = [
		16, 7, 20, 21,
	    29, 12, 28, 17,
	    1, 15, 23, 26,
	    5, 18, 31, 10,
	    2, 8, 24, 14,
	    32, 27, 3, 9,
	    19, 13, 30, 6,
	    22, 11, 4, 25
		]

def toBinary(tex):
	binlist = []

	for x in tex:
		binlist.append(int(format(ord(x), 'b').zfill(8), 2))
	return binlist

def strTo32(bit_string,bits):
	while bit_string:
		yield bit_string[:bits]
		bit_string = bit_string[bits:]

def getKeySchedule(key):
    """Returns key schedule of 44 words
    :param key: 64 bit master key
    :return: key schedule
    """
    
    # key_schedule = rotate_matrix(key_schedule)
    key_expanded = []
    key_schedule = deque(key)
    for i in range(16):
        key_schedule.rotate(-2)
        key_expanded.append(list(key_schedule)[:3] + list(key_schedule)[4:])
    return key_expanded

def pkcsPadding(text):
	tlen = 8 - (len(text)%8)
	text += tlen*chr(tlen)
	return(text)

def performXor(array_1, array_2):
	added_key = list(map(xor,array_1,array_2))
	return added_key

def byteSplit(array):
	return array[:4], array[4:]

def expansion(array):
	bin_string = ''
	fin_string = ''
	j = 0
	for i in array:
		bin_string += bin(i)[2:].zfill(8)
	for i in range(8):
		x = '{}{}{}'.format(bin_string[(31+j)%32], bin_string[j:j+4], bin_string[(j+4)%32])
		fin_string += x
		j += 4
	fin_string = list(strTo32(fin_string, 8))
	for n,i in enumerate(fin_string):
		fin_string[n] = int(i, 2)
	return(fin_string)

def substitution(array):
	bin_string = ''
	for i in array:
		bin_string += bin(i)[2:].zfill(8)
	array = list(strTo32(bin_string, 6))
	sub_arr = []
	j = 0
	for i in array:
		r = int('{}{}'.format(i[:1], i[5:]),2)
		c = int(i[1:5],2)
		sub_arr.append(sboxes[j][16*r+c])
		j = j+1

	return sub_arr

def permutation(array):
	bin_string = ''
	bin_pos = {}
	fin_string = ''
	for i in array:
		bin_string += bin(i)[2:].zfill(4)
	for i in range(32):
		fin_string += bin_string[perm[i]-1]
	fin_array = list(strTo32(fin_string,8))
	for n,i in enumerate(fin_array):
		fin_array[n] = int(i,2)

	return fin_array

def feistel(str_array, key_array):
	str_array = expansion(str_array)
	str_array = performXor(str_array, key_array)
	str_array = substitution(str_array)
	str_array = permutation(str_array)
	return(str_array)

def feistel_network(str_array, key, decrypt = False):
	key_schedule = getKeySchedule([249,137,235,15,244,240,25])
	if(decrypt == True):
		key_schedule.reverse()
	l,r = byteSplit(str_array)

	for i in range(16):
		feistel_output = feistel(r, key_schedule[i])
		feistel_output = performXor(l, feistel_output)
		l = r
		r = feistel_output

	return r+l

def cbc_encrypt(plaintext, key, init_vector = 'abcdefgh'):
	str_array = toBinary(pkcsPadding(plaintext))
	str_array = [str_array[i*8:(i+1)*8] for i in range((len(str_array)+7)//8)]
	init_vector = toBinary(init_vector) 

	cipherblocks = []
	ciphertext = ''

	for i in range(len(str_array)):
		ciph_block = performXor(str_array[i], init_vector)
		ciph_block = feistel_network(ciph_block, key)
		cipherblocks.append(ciph_block)
		init_vector = ciph_block

	cipherblocks = [item for sublist in cipherblocks for item in sublist]

	ciphertext = ' '.join(bin(i)[2:].zfill(8) for i in cipherblocks)

	output_file = open('ciphertext.txt','w')
	output_file.write(ciphertext)
	output_file.close()

def cbc_decrypt(ciphertext, key, init_vector="abcdefgh"):
	str_array = ciphertext.split(' ')
	for n,i in enumerate(str_array):
		str_array[n] = int(i,2)
	str_array = [str_array[i*8:(i+1)*8] for i in range((len(str_array)+7)//8)]
	init_vector = toBinary(init_vector)

	cipherblocks = []
	ciphertext = ''

	for i in range(len(str_array)):
		ciph_block = feistel_network(str_array[i], key, decrypt=True)
		ciph_block = performXor(ciph_block, init_vector)
		cipherblocks.append(ciph_block)
		init_vector = str_array[i]

	cipherblocks = [item for sublist in cipherblocks for item in sublist]

	ciphertext = ' '.join(bin(i)[2:].zfill(8) for i in cipherblocks)
	ciphertext = ''.join([chr(int(s, 2)) for s in ciphertext.split()])

	output_file = open('plaintext.txt','w')
	output_file.write(ciphertext)
	output_file.close()

#filename = sys.argv[1] # get file name from params
input_text = (open('ciphertext.txt').read()).replace('\n','') # remove newline characters
#keyfilename = sys.argv[2]
key_text = (open('key.txt').read()).replace('\n','')
print (key_text)
op_mode = input()

if op_mode == 'e':
	cbc_encrypt(input_text,key_text)
elif op_mode == 'd':
	cbc_decrypt(input_text,key_text)

