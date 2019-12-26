import RSA_utils as belt

data = belt.file_read("public_key.txt")
pubkey = int(data[0].rstrip())
n = int(data[1].rstrip())

data = belt.file_read("private_key.txt")
prikey = int(data[0])

ciphertext = list(belt.file_read("ciphertext.txt"))

plaintext = belt.mod_pow(int(ciphertext[0]),prikey,n)

belt.file_write("decipher.txt",str(plaintext))