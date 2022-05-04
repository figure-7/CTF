from Crypto.Util.number import *

def decrypt(c):
    #4
    c = c[:19] + bin(eval('0b' + c[19:]) ^ eval('0b' + c[:13]))[2:].zfill(13)
    #3
    f = bin(2245263360)[2:].zfill(32)
    c1 = c[-17:]
    c2 =  bin(eval('0b' + c[:-17]) ^ (eval('0b' + c1[-15:]) & eval('0b' + f[:-17])))[2:].zfill(15)
    c = c2 + c1
    #2
    f = bin(2029229568)[2:].zfill(32)
    c1 = c[-9:]
    f = f[:-9]
    c2 = bin(eval('0b' + c[-18:-9]) ^ (eval('0b' + c1) & eval('0b' + f[-9:])))[2:].zfill(9)
    f = f[:-9]
    c3 = bin(eval('0b' + c[-27:-18]) ^ (eval('0b' + c2) & eval('0b' + f[-9:])))[2:].zfill(9)
    f = f[:-9]
    c4 = bin(eval('0b' + c[:5]) ^ (eval('0b' + c3[-5:]) & eval('0b' + f[-5:])))[2:].zfill(5)
    c = c4 + c3 + c2 + c1
    #1
    c_1 = c[:13]
    c_2 = bin(eval('0b' + c_1) ^ eval('0b' + c[13:26]))[2:].zfill(13)
    c_3 = bin(eval('0b' + c_2[:6]) ^ eval('0b' + c[-6:]))[2:].zfill(6)
    c = c_1 + c_2 + c_3
    return c

message = '641460a9e3953b1aaa21f3a2'

m = ''
for i in range(0,len(message),8):
    txt = bin(eval('0x' + message[i:i+8]))[2:].zfill(32)
    m += decrypt(txt)

m = hex(eval('0b'+m))[2:]
    
print(m)
#84b45f89af22ce7e67275bdc
