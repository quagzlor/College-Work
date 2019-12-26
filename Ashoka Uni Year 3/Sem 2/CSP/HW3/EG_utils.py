import random

def gcd(x,y): #Greatest Common Divisor
    while y != 0:
        x,y = y,x % y
    return x

def mod_pow(x,y,z): #Modular power
    val = 1

    while y:
        if y & 1:
            val = val * x % z
        y >>= 1
        x = x * x % z
    return val

def prime_check(num): #Checks for prime
    if num == 2:
        return True
    elif num<2 or num%2 == 0:
        return False
    r,s = 0,num-1

    while s%2 == 0:
        r= r+1
        s >>1
    for i in range(50):
        x = random.randrange(2,num-1)
        y = mod_pow(x,s,num)
        if y == 1 or y == num - 1:
            continue
        for j in range(r-1):
            y = mod_pow(y,2,num)

            if y == num - 1:
                break
        else:
            return False
    return True

def primitive_root(p):
    if p==2:
        return 1
    x = 2
    y = (p-1) // x

    while (True):
        root = random.randint(2,p-1)

        if mod_pow(root,(x-1)//x,p) != 1:
            if mod_pow(root,(x-1)//y,p) != 1:
                return root