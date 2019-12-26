import numpy as np
from scipy import linalg as sci
import math

def quad_residue(n):
    residue = []
    for i in range(n):
        residue.append((i**2 % n))
    x = np.array(residue)
    x = np.unique(x)

    return x
        
def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def q_matrix_3(n):

    residue = quad_residue(n)
    array = np.zeros((n,n))
    for i in range(1,(n)):
        for j in range(1,(n)):
            array[i][j] =  (j-i)
            if (array[i][j] == 0):
                array[i][j] = -1
            elif array[i][j] in residue:
                array[i][j] = 1
            else:
                array[i][j] = -1
    array[:,0] = 1
    array[0][:] = 1

    return array

def q_matrix_1(n):
    array = np.zeros((n,n))
    for i in range(1,(n)):
        for j in range(1,(n)):
            array[i][j] =  (j-i)
            if (array[i][j] == 0):
                array[i][j] = -1
            elif array[i][j] in residue:
                array[i][j] = 1
            else:
                array[i][j] = -1
    array[:,0] = 1
    array[0][:] = 1
    array[0][0] = 0

    return array
    
def main():    
    print ("Enter N")
    n= int(input())

    n_is_power = math.log10(n)/math.log10(2)

    if (math.ceil(n_is_power) == math.floor(n_is_power)):
        print ("Sylvester construction \n")
        np_arr=sci.hadamard(n)
        print (np_arr)
        
    elif(n%4 == 3):
        if is_prime(n):
            x = q_matrix_3(n)
            print (x)
        else:
            print ("Does not exist")
        
    elif(n%4 == 1):
        if is_prime(n):
            x = Paley2(n)
            print (x)
        else:
            print ("Does not exist")
        
    elif(n%4 == 0):
        print ("May be possible")
        
    elif(n == 1):
        print ("[1]")
        
    else:
        print ("Does not exist")
        
main()
