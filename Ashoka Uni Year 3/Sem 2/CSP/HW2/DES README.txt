Padding used : PKCS#5

You can select between encryption and decryption by entering '1' for encryption, and '2' for decryption when prompted.

------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------

Encryption mode:

Key reads from: key.txt
Plaintext reads from: plaintext.txt

Ensure both key and plaintext are in ASCII characters.

The initialisation vector must be input when prompted.

The output will be in binary, in "encrypted.txt"
I tried converting it to text, but didn't work and i'm tired.

------------------------------------------------------------------------------------------------------------------------

Decryption mode:

Key reads from key.txt
Ciphertext reads from: encrypted.txt

Ensure key is in ASCII, and ciphertext is in 8-bit binary.

The initialisation vector must be input when prompted.

The output will be in ASCII, in "decrypted.txt"