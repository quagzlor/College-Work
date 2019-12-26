import EG_utils as belt
import random

def pq_gen():
    p = random.getrandbits(20)
    if p%2 == 0:
        p = p-1

    while belt.prime_check(p)!= True:
        p = p-2

        if p<(p**299):
            pq_gen()
    q = 2*p -1

    if belt.prime_check(q) != True:
        pq_gen()

    return p,q

p,q = pq_gen()

print (p)
print (q)