import random

def multiplicative_inverse(e,phi): #Multiplicative inverse function
    phi_0 = phi
    y = 0
    x = 1

    while (e > 1):
        quotient = e//phi
        temp = phi
        phi = e%phi
        e = temp
        temp = y

        y = x - quotient*y
        x = temp
    if (x<0):
        x = x + phi_0

    return x

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
        s //=2
    for i in range(40):
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

def file_write(filename,data):
    writer = open(filename,'w')
    writer.writelines(data)

    writer.close()

def file_read(filename):
    reader = open(filename,'r')
    data = reader.readlines()

    reader.close()

    return data
