import gmpy2
from Crypto.Util.number import *
from binascii import a2b_hex,b2a_hex

flag = "*****************"

flag = flag.encode()

p = 262248800182277040650192055439906580479
q = 262854994239322828547925595487519915551

e = 65533
n = p*q


c = pow(int(b2a_hex(flag),16),e,n)

print (c)

# 27565231154623519221597938803435789010285480123476977081867877272451638645710
