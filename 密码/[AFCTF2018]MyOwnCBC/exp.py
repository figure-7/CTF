'''
#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from Crypto.Cipher import AES
from Crypto.Random import random
from Crypto.Util.number import long_to_bytes

def MyOwnCBC(key, plain):
	if len(key)!=32:
		return "error!"
	cipher_txt = b""
	cipher_arr = []
	cipher = AES.new(key, AES.MODE_ECB, "")
	plain = [plain[i:i+32] for i in range(0, len(plain), 32)]
	print plain
	cipher_arr.append(cipher.encrypt(plain[0]))
	cipher_txt += cipher_arr[0]
	for i in range(1, len(plain)):
		cipher = AES.new(cipher_arr[i-1], AES.MODE_ECB, "")
		cipher_arr.append(cipher.encrypt(plain[i]))
		cipher_txt += cipher_arr[i]
	return cipher_txt

key = random.getrandbits(256)
key = long_to_bytes(key)

s = ""
with open("flag.txt","r") as f:
	s = f.read()
	f.close()

with open("flag_cipher","wb") as f:
	f.write(MyOwnCBC(key, s))
	f.close()

'''
import Crypto.Cipher.AES
with open('flag_cipher','rb') as f:
    cipher=f.read()
    f.close()
key0=cipher[0:32]
def decrypt(key0,cipher):
    cipher=[cipher[i:i+32] for i in range(0,len(cipher),32)]
    tempkey=key0
    plain = b''
    for i in range(1,len(cipher)):
        aes=Crypto.Cipher.AES.new(tempkey,Crypto.Cipher.AES.MODE_ECB)
        plain+=aes.decrypt(cipher[i])
        tempkey=cipher[i]
    return plain
print(decrypt(key0,cipher))

#afctf{Don't_be_fooled_by_yourself}
