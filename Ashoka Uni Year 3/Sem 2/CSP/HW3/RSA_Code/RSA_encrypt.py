import RSA_utils as belt

data = belt.file_read("public_key.txt")
key = int(data[0].rstrip())
n = int(data[1].rstrip())

plaintext = belt.file_read("plaintext.txt")
plaintext = int(plaintext[0])

ciphertext = belt.mod_pow(plaintext,key,n)

belt.file_write("ciphertext.txt", str(ciphertext))