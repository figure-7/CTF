from Crypto.Util.number import *

p=262248800182277040650192055439906580479
q=262854994239322828547925595487519915551
c=27565231154623519221597938803435789010285480123476977081867877272451638645710
n=p*q
e=65533
phi=(p-1)*(q-1)
d = inverse(e,phi)

print (long_to_bytes(pow(c,d,n)))
