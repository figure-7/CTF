from random import Random

def invert_right(m,l,val=''):
    length = 32
    mx = 0xffffffff
    if val == '':
        val = mx
    i,res = 0,0
    while i*l<length:
        mask = (mx<<(length-l)&mx)>>i*l
        tmp = m & mask
        m = m^tmp>>l&val
        res += tmp
        i += 1
    return res

def invert_left(m,l,val):
    length = 32
    mx = 0xffffffff
    i,res = 0,0
    while i*l < length:
        mask = (mx>>(length-l)&mx)<<i*l
        tmp = m & mask
        m ^= tmp<<l&val
        res |= tmp
        i += 1
    return res

def invert_temper(m):
    m = invert_right(m,18)
    m = invert_left(m,15,4022730752)
    m = invert_left(m,7,2636928640)
    m = invert_right(m,11)
    return m

def clone_mt(record):
    state = [invert_temper(i) for i in record]
    gen = Random()
    gen.setstate((3,tuple(state+[0]),None))
    return gen


f = open("random.txt",'r').readlines()
prng = []
j=0
for i in f:
    i = i.strip('\n')
    print(int(i).bit_length())
    if(j%3==0):
        prng.append(int(i))
    elif(j%3==1):#将生成两次随机数的两个随机数分离出来
        prng.append(int(i)& (2 ** 32 - 1))
        prng.append(int(i)>> 32)
    else:#将生成三次随机数的三个随机数分离出来
        prng.append(int(i)& (2 ** 32 - 1))
        prng.append(int(i)& (2 ** 64 - 1) >> 32)
        prng.append(int(i)>>64)
    j+=1

g = clone_mt(prng[:624])
for i in range(624):
    g.getrandbits(32)#产生前624个随机数，让state状态到生成flag前

key = g.getrandbits(32)
print(key)
from hashlib import md5
flag = md5(str(key).encode()).hexdigest()
print(flag)
#14c71fec812b754b2061a35a4f6d8421
