from base64 import b64encode as b32encode
from base64 import b64decode as b32decode
import gmpy2
from Crypto.Util.number import *
from binascii import a2b_hex,b2a_hex
import random

p = 177077389675257695042507998165006460849
n = 37421829509887796274897162249367329400988647145613325367337968063341372726061
c = '==gMzYDNzIjMxUTNyIzNzIjMyYTM4MDM0gTMwEjNzgTM2UTN4cjNwIjN2QzM5ADMwIDNyMTO4UzM2cTM5kDN2MTOyUTO5YDM0czM3MjM'
c = str(c)[::-1]
print(b32decode(str(c)))
#c = 2373740699529364991763589324200093466206785561836101840381622237225512234632
q = n //p
#q = 211330365658290458913359957704294614589
phi = (q-1) * (p-1)
e = random.randint(50000,70000)
for e in range(50000,70000):
	if gmpy2.gcd(e,phi) == 1:
		d = gmpy2.invert(e ,phi)
		m = pow(c,d,n)
		if 'flag' in str(long_to_bytes(m)):
			print('e = ',e)
			print(long_to_bytes(m))
			break
# e =  51527
# b'flag{rs4_1s_s1mpl3!#}'
