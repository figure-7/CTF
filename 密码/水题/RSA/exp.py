from Crypto.Util.number import *

p = 473398607161
q = 4511491
e = 17

phi = (p - 1) * (q - 1)
d=inverse(e,phi)
print(d)
