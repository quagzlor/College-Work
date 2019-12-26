from collections import Counter #Number of times an alphabet occurs in a string
import operator

eng_freq = {
    'a' : 0.08167,
    'b' : 0.01492,
    'c' : 0.02782,
    'd' : 0.04253,
    'e' : 0.12702,
    'f' : 0.02228,
    'g' : 0.02015,
    'h' : 0.06094,
    'i' : 0.06966,
    'j' : 0.00153,
    'k' : 0.00772,
    'l' : 0.04025,
    'm' : 0.02406,
    'n' : 0.06749,
    'o' : 0.07507,
    'p' : 0.01929,
    'q' : 0.00095,
    'r' : 0.05987,
    's' : 0.06327,
    't' : 0.09056,
    'u' : 0.02758,
    'v' : 0.00978,
    'w' : 0.0236,
    'x' : 0.0015,
    'y' : 0.01974,
    'z' : 0.00074}
alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def chi_sqr(key): #performs the chi square operation
    freq = Counter(key)

    score = 0

    for counter_key, counter_val in freq.items():
        score = score + (((counter_val-(len(key)*(eng_freq[counter_key]/100)))**2)/(len(key)*(eng_freq[counter_key]/100))) #Chi square score

    return score

def shift_crack(cryptograms): #Runs chi-square method on each cryprogram
    best_fits = []


    for crypto in cryptograms:
        shifted = {}
        
        for i in range(26): #Makes 26 possible versions of the cipher block
            deciphered_text = ""

            for j in crypto:
                deciphered_text = deciphered_text + alpha_list[(alpha_list.index(j)+i)%26]

            shifted[deciphered_text] = chi_sqr(deciphered_text)

        best_fits.append(min(zip(shifted.values(), shifted.keys()))) #Appends the lowest chi square score (ie clsoest to english language)
    return best_fits


def main(): #Brute forces all possible combinations
    print ("Enter ciphertext")

    ciphertext = input()
    ciphertext = ciphertext.replace(" ","")
    key_len = 0

    for i in range(6):
        key_len = key_len + 1

        cryptograms = [ciphertext[chunk::key_len] for chunk in range(key_len)] #divides the cipher text into blocks of length 1-6

        cracked_cipher = shift_crack(cryptograms)

        cracked_message = ""

        for j in range(len(cracked_cipher[0][1])): #Puts the string back together properly
            for k in range(len(cracked_cipher)):
                if j < len(cracked_cipher[k][1]):
                    cracked_message = cracked_message + cracked_cipher[k][1][j]
        

        print ("For key length" + str(i+1) + ":")
        print ("\n")
        print (cracked_message)
        print ("\n")

    cryptograms = [ciphertext[i::]]
    ciphertext.replace (" ","")
main()