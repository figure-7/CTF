'''
from Crypto.Util.number import *
from gmpy2 import *
from secret import flag

p = getPrime(25)
e = # Hidden
q = getPrime(25)
n = p * q
m = bytes_to_long(flag.strip(b"npuctf{").strip(b"}"))

c = pow(m, e, n)
print(c)
print(pow(2, e, n))
print(pow(4, e, n))
print(pow(8, e, n))

'''
169169912654178
128509160179202
518818742414340
358553002064450
'''


'''
c=169169912654178
a1=128509160179202
a2=518818742414340
a3=358553002064450
import gmpy2
print(gmpy2.gcd(a1**2-a2,a1*a2-a3))
p=18195301
q=28977097
n=p*q
import sympy
e=sympy.discrete_log(n,a1,2)
d=gmpy2.invert(e,(p-1)*(q-1))
import Crypto.Util.number
print(Crypto.Util.number.long_to_bytes(gmpy2.powmod(c,d,n)))


