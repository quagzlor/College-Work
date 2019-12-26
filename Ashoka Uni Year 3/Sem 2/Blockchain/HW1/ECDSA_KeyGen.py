#Author: Divij Gurpreet Singh
from ecdsa import SigningKey, SECP256k1

def write(filename,info):
    writer = open(filename,'w')
    writer.write(info)

    writer.close()

private_key = SigningKey.generate(curve=SECP256k1)
public_key = private_key.get_verifying_key()

write("skhex.txt",str(private_key.to_string().hex()))
write("skpem.txt",str(private_key.to_pem()))

write("pkhex.txt",str(public_key.to_string().hex()))
write("pkpem.txt",str(public_key.to_pem()))