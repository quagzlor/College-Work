import RSA_utils as belt
import random

#Generating primes
p = random.getrandbits(514)
q = random.getrandbits(514)

if p%2 == 0:
    p = p-1

if q%2 == 0:
    q = q-1

while not(belt.prime_check(p)):
    p = p-2

while not(belt.prime_check(q)):
    q = q-2

n = p*q

phi = (p-1)*(q-1)

e = random.randrange(1,phi)
g = belt.gcd(e,phi)

while g!= 1: #Verify that e and phi are coprime
    e = random.randrange(1,phi)
    g = belt.gcd(e,phi)

d = belt.multiplicative_inverse(e,phi)

public_key = str(e) + "\n" + str(n)

belt.file_write("public_key.txt", public_key)
belt.file_write("private_key.txt", str(d))