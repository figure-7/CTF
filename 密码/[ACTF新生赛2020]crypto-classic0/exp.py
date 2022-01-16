cipher='Ygvdmq[lYate[elghqvakl}'
 
for i in range(0,24):
    flag=ord(cipher[i]) ^ 0x7
    flag += 3
    print ( chr(flag),end='' )
