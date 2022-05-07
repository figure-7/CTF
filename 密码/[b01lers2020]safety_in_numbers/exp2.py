from Crypto.Util.number import *
import base64
import gmpy2
key_end_base64="l8UvtaFCpNsgheCRz1j+HD9cHH05ozrbHMe/rtEUQa6fmQcAJbDNBXZV+yabO1aSKwVm5ZgHKQIDAQAB"
key=base64.b64decode(key_end_base64)
print(hex(bytes_to_long(key)))
f=open("flag.enc","rb")
c_bytes=f.read()
c=int.from_bytes(c_bytes,byteorder="little")
m=gmpy2.iroot(c,0x10001)[0]
flag=long_to_bytes(m)[::-1]
print(flag)
