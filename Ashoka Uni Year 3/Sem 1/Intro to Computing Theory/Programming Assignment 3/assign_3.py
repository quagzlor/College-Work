from komm._error_control_block import BCHCode as bch

print ("Input r")
r = int(input())

kommando = bch(r,2)

print ("[n,k,d] = " ,kommando.length, kommando.dimension, kommando.minimum_distance)

print ("Generator Matrix:")
print (kommando.generator_matrix)

print ("Parity Check Matrix:")
print (kommando.parity_check_matrix)

print ("Enter the message")
en_message = (input())
encoded = kommando.encode(en_message)
print ("Encoded message: ",encoded)


print ("Enter the message to decode")
de_message = int(input())
decoded = kommando.decode(de_message)
print ("Decoded message: ", decoded)
