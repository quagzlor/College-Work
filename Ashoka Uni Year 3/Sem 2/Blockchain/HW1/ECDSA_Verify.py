from ecdsa import VerifyingKey, BadSignatureError, SECP256k1
import binascii

def reader(filename,read_type):
    reader = open(filename,read_type)
    info = reader.read()
    reader.close()

    return info

hex_key = reader("pkhex.txt","r")
hex_key = binascii.unhexlify(hex_key)

public_key = VerifyingKey.from_string(hex_key, curve = SECP256k1)

message = reader("msg.txt","rb")

signature = reader("sighex.txt","r")
signature = binascii.unhexlify(signature)

try: 
    public_key.verify(signature,message)
    print ("Valid")
except BadSignatureError:
    print ("Invalid")