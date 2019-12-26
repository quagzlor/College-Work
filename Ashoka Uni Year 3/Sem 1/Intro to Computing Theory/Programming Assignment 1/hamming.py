import numpy as nunu
import math

def matrix_gen(r,n,k):
    M = []
    for i in range(1,(n+1)):
        binary_num = bin(i)[2:]
        length = len(binary_num)
        M.append([int(char) for char in str("0" *(r-length) + binary_num)])
    #print (M)
    for i in range(0,r):
        temp=M[i]
        M[i]=M[(2**i)-1]
        M[(2**i)-1] = temp
    #print (M)
    return nunu.array(M).T

def gen_gen(H,r,nk): 
    H_list = H[:,r:].T    
    G_I = nunu.identity(H_list.shape[0])
    print (H_list)

    G= nunu.hstack((G_I,H_list))
  
    return G

print ("Please enter the parameter")
param_r= int(input())

param_n = (2**param_r) - 1
param_k = (2**param_r) - param_r - 1
param_d = 3

H_temp = matrix_gen(param_r,param_n,param_k)
H_temp_2 = nunu.fliplr(H_temp)
H = H_temp_2.tolist()

G = (gen_gen(H_temp,param_r,(param_n - param_k))).tolist()

print ("Generator matrix is: \n" + str(nunu.array(G)))
print ("Parity matrix is: \n" + str(nunu.array(H)))

print ("Enter the message to encode")
encode_string = [int(i) for i in input()]

encoded_message = (nunu.array(encode_string)).dot(nunu.array(G))

for i in range(len(encoded_message)):
    encoded_message[i]=encoded_message[i]%2

print ("The encoded message is: " + str(encoded_message))


print ("Enter the message to decode")
decode_string = [int(i) for i in input()]
decode_array = nunu.array(decode_string)

dot_prod = nunu.dot(H,decode_array.T)

syndrome = 0
for i in range(len(dot_prod)):
    syndrome = syndrome*10 + dot_prod[i]%2
print (syndrome)

location = len(decode_array) - int(str(syndrome),2)

if (decode_array[location-1] == 1):
    decode_array[location-1] = 0
else:
    decode_array[location-1] = 1

parity = len(decode_array)

decoded = ""

for i in range(len(decode_array)-1,-1,-1):
    if(i!=(parity-1)):
        decoded = decoded + str(decode_array[i])
    else:
        parity = parity / 2
    
print ("The decoded message is: " + str(decoded))
