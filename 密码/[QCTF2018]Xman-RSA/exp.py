
'''
from gmpy2 import is_prime
from os import urandom
import base64

def bytes_to_num(b):
    return int(b.encode('hex'), 16)
def num_to_bytes(n):
    b = hex(n)[2:-1]
    b = '0' + b if len(b) % 2 == 1 else b
    return b.decode('hex')
def get_a_prime(l):
    random_Teed = urandom(l)
    num = bytes_to_num(random_Teed)
    while True:
          if is_prime(num):
                   break
          num+= 1
    return num

def encrypt(s, e, n):
    p = bytes_to_num(s)
    p = pow(p, e, n)
    return num_to_bytes(p).encode('hex')
def separate(n):
    p = n % 4
    t = (p * p) % 4
    return t == 1
f = open('flag.txt', 'r')
flag = f.read()
msg1 = ""
msg2 = ""
for i in range(len(flag)):
    if  separate(i):
            msg2 += flag[i]
    else:
           msg1 += flag[i]
p1 = get_a_prime(128)
p2 = get_a_prime(128)
p3 = get_a_prime(128)
n1 = p1 * p2
n2 = p1 * p3
e = 0x1001
c1 = encrypt(msg1, e, n1)
c2 = encrypt(msg2, e, n2)
print(c1)
print(c2)
e1 = 0x1001
e2 = 0x101
p4 = get_a_prime(128)
p5 = get_a_prime(128)
n3 = p4 * p5
c1 = num_to_bytes(pow(n1, e1, n3)).encode('hex')
c2 = num_to_bytes(pow(n1, e2, n3)).encode('hex')
print(c1)
print(c2)
print(base64.b64encode(num_to_bytes(n2)))
print(base64.b64encode(num_to_bytes(n3)))
'''
e1 = 0x1001
e2 = 0x101
e = 0x1001
n2='PVNHb2BfGAnmxLrbKhgsYXRwWIL9eOj6K0s3I0slKHCTXTAUtZh3T0r+RoSlhpO3+77AY8P7WETYz2Jzuv5FV/mMODoFrM5fMyQsNt90VynR6J3Jv+fnPJPsm2hJ1Fqt7EKaVRwCbt6a4BdcRoHJsYN/+eh7k/X+FL5XM7viyvQxyFawQrhSV79FIoX6xfjtGW+uAeVF7DScRcl49dlwODhFD7SeLqzoYDJPIQS+VSb3YtvrDgdV+EhuS1bfWvkkXRijlJEpLrgWYmMdfsYX8u/+Ylf5xcBGn3hv1YhQrBCg77AHuUF2w/gJ/ADHFiMcH3ux3nqOsuwnbGSr7jA6Cw=='
n3='TmNVbWUhCXR1od3gBpM+HGMKK/4ErfIKITxomQ/QmNCZlzmmsNyPXQBiMEeUB8udO7lWjQTYGjD6k21xjThHTNDG4z6C2cNNPz73VIaNTGz0hrh6CmqDowFbyrk+rv53QSkVKPa8EZnFKwGz9B3zXimm1D+01cov7V/ZDfrHrEjsDkgK4ZlrQxPpZAPl+yqGlRK8soBKhY/PF3/GjbquRYeYKbagpUmWOhLnF4/+DP33ve/EpaSAPirZXzf8hyatL4/5tAZ0uNq9W6T4GoMG+N7aS2GeyUA2sLJMHymW4cFK5l5kUvjslRdXOHTmz5eHxqIV6TmSBQRgovUijlNamQ=='
c11=0x2639c28e3609a4a8c953cca9c326e8e062756305ae8aee6efcd346458aade3ee8c2106ab9dfe5f470804f366af738aa493fd2dc26cb249a922e121287f3eddec0ed8dea89747dc57aed7cd2089d75c23a69bf601f490a64f73f6a583081ae3a7ed52238c13a95d3322065adba9053ee5b12f1de1873dbad9fbf4a50a2f58088df0fddfe2ed8ca1118c81268c8c0fd5572494276f4e48b5eb424f116e6f5e9d66da1b6b3a8f102539b690c1636e82906a46f3c5434d5b04ed7938861f8d453908970eccef07bf13f723d6fdd26a61be8b9462d0ddfbedc91886df194ea022e56c1780aa6c76b9f1c7d5ea743dc75cec3c805324e90ea577fa396a1effdafa3090
c22=0x42ff1157363d9cd10da64eb4382b6457ebb740dbef40ade9b24a174d0145adaa0115d86aa2fc2a41257f2b62486eaebb655925dac78dd8d13ab405aef5b8b8f9830094c712193500db49fb801e1368c73f88f6d8533c99c8e7259f8b9d1c926c47215ed327114f235ba8c873af7a0052aa2d32c52880db55c5615e5a1793b690c37efdd5e503f717bb8de716303e4d6c4116f62d81be852c5d36ef282a958d8c82cf3b458dcc8191dcc7b490f227d1562b1d57fbcf7bf4b78a5d90cd385fd79c8ca4688e7d62b3204aeaf9692ba4d4e44875eaa63642775846434f9ce51d138ca702d907849823b1e86896e4ea6223f93fae68b026cfe5fa5a665569a9e3948a
c1=0x1240198b148089290e375b999569f0d53c32d356b2e95f5acee070f016b3bef243d0b5e46d9ad7aa7dfe2f21bda920d0ac7ce7b1e48f22b2de410c6f391ce7c4347c65ffc9704ecb3068005e9f35cbbb7b27e0f7a18f4f42ae572d77aaa3ee189418d6a07bab7d93beaa365c98349d8599eb68d21313795f380f05f5b3dfdc6272635ede1f83d308c0fdb2baf444b9ee138132d0d532c3c7e60efb25b9bf9cb62dba9833aa3706344229bd6045f0877661a073b6deef2763452d0ad7ab3404ba494b93fd6dfdf4c28e4fe83a72884a99ddf15ca030ace978f2da87b79b4f504f1d15b5b96c654f6cd5179b72ed5f84d3a16a8f0d5bf6774e7fd98d27bf3c9839
c2=0x129d5d4ab3f9e8017d4e6761702467bbeb1b884b6c4f8ff397d078a8c41186a3d52977fa2307d5b6a0ad01fedfc3ba7b70f776ba3790a43444fb954e5afd64b1a3abeb6507cf70a5eb44678a886adf81cb4848a35afb4db7cd7818f566c7e6e2911f5ababdbdd2d4ff9825827e58d48d5466e021a64599b3e867840c07e29582961f81643df07f678a61a9f9027ebd34094e272dfbdc4619fa0ac60f0189af785df77e7ec784e086cf692a7bf7113a7fb8446a65efa8b431c6f72c14bcfa49c9b491fb1d87f2570059e0f13166a85bb555b40549f45f04bc5dbd09d8b858a5382be6497d88197ffb86381085756365bd757ec3cdfa8a77ba1728ec2de596c5ab
import base64
import Crypto.Util.number
n2=Crypto.Util.number.bytes_to_long(base64.b64decode(n2))
n3=Crypto.Util.number.bytes_to_long(base64.b64decode(n3))
import  gmpy2
import  binascii
import  rsa
import math
def exgcd(m, n, x, y):
    if n == 0:
        x = 1
        y = 0
        return (m, x, y)
    a1 = b = 1
    a = b1 = 0
    c = m
    d = n
    q = int(c / d)
    r = c % d
    while r:
        c = d
        d = r
        t = a1
        a1 = a
        a = t - q * a
        t = b1
        b1 = b
        b = t - q * b
        q = int(c / d)
        r = c % d
    x = a
    y = b
    return (d, x, y)#扩展欧几里得算法
def separate(n):
    p = n % 4
    t = (p * p) % 4
    return t == 1
ans=exgcd(e1,e2,0,0)
s1=ans[1]
s2=ans[2]
n1=(gmpy2.powmod(c11,s1,n3)*gmpy2.powmod(c22,s2,n3))%n3#powmod()函数真香,分数取模也可直接算,一开始不知道还去找了很多的算法知识
p1=gmpy2.gcd(n1,n2)
p2=n1//p1
p3=n2//p1
phi1=(p1-1)*(p2-1)
phi2=(p1-1)*(p3-1)
d1=gmpy2.invert(e,phi1)
d2=gmpy2.invert(e,phi2)
m1=gmpy2.powmod(c1,d1,n1)
m2=gmpy2.powmod(c2,d2,n2)
m1=Crypto.Util.number.long_to_bytes(m1).decode()
m2=Crypto.Util.number.long_to_bytes(m2).decode()
length=len(m1)+len(m2)
flag=''
temp1=0
temp2=0
for i in range(length):
    if separate(i):
        flag+=m2[temp2]
        temp2=temp2+1
    else:
        flag+=m1[temp1]
        temp1=temp1+1
print(flag)







