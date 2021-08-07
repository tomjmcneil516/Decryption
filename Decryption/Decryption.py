import sys

plaintext = open(sys.argv[3], "wb")
keyfile = open(sys.argv[1], "rb")
ciphertext = open(sys.argv[2], "rb")

ciphertext_byte = ciphertext.read(1)
keyfile_byte = keyfile.read(1)

while ciphertext_byte:
    plaintext_byte = ((sum(bytearray(ciphertext_byte)) - sum(bytearray(keyfile_byte))) % 256).to_bytes(1,'big')
    plaintext.write(plaintext_byte)
    ciphertext_byte = ciphertext.read(1)
    keyfile_byte = keyfile.read(1)
    if not keyfile_byte:
        keyfile.seek(0)
        keyfile_byte = keyfile.read(1)

plaintext.close()
keyfile.close()
ciphertext.close()