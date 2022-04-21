import gmpy2
import hashlib
n = 523798549
p = 10663
q = 49123
c = 162853095
yxm = 110001

gcd = gmpy2.gcdext(p,q)
s,t = int(gcd[1]),int(gcd[2])

mp = pow(c,(p+1)//4,p)
mq = pow(c,(q+1)//4,q)

m1 = (s*p*mq + t*q*mp)%n
print(bin(m1)[2:])
m2= n - m1
print(bin(m2)[2:])
m3 = (s*p*mq - t*q*mp)%n
print(bin(m3)[2:])
m4 = n - m3
print(bin(m4)[2:])
#判断   是第一个

flag = int(bin(m1)[2:-6],2)
print(flag)
print(hashlib.md5(str(flag).encode()).hexdigest())
