from ecdsa import SigningKey, SECP256k1
import binascii

def reader(filename,read_type):
    reader = open(filename,read_type)
    info = reader.read()
    reader.close()

    return info

def write_pem(info):
    writer = open("sigpem.txt","w")
    writer.write("-----BEGIN SIGNATURE-----\\n")
    writer.write(info)
    writer.write("\\n-----END SIGNATURE-----\\n")
    writer.close()

def write_hex(info):
    writer = open("sighex.txt","w")
    writer.write(info)
    writer.close()

hex_key = reader("skhex.txt","r")
hex_key = binascii.unhexlify(hex_key)

private_key = SigningKey.from_string(hex_key,curve = SECP256k1)

message = reader("msg.txt","rb")

signature = private_key.sign(message)

write_pem(str(signature))

write_hex(signature.hex())