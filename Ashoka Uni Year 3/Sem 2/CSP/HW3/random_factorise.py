import random

def gcd(x,y): #Greatest Common Divisor
    while y != 0:
        x,y = y,x % y
    return x

def mod_pow(x,y,z):
    val = 1

    while y:
        if y & 1:
            val = val * x % z
        y >>= 1
        x = x * x % z
    return val

n = 1501
e = 323
d = 539

s = 0
t = (e*d) - 1

while (t%2 == 0):
    s = s + 1
    t = t/2

flag = False   

while (flag != True):
    a = random.randint(1,n)

    b = mod_pow(a,int(t),n)

    while (mod_pow(b,2,n) != 1 ):
        b = mod_pow(b,2,n)
    if ((b % n)**2 != 1):
        flag = True
p = gcd(b-1,n)
q = int(n/p)

phi_n = (p-1)*(q-1)

print ("Phi N :" + str(phi_n))
print ("P=" + str(p))
print ("Q=" + str(q))

if (e*d)%phi_n == 1:
    print ("Answer is true")