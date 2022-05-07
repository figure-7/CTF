#!python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/26 12:48
# @Author : A.James
# @FileName: tt2.py
from Crypto.Util.number import *
import base64
c = 'KwVm5ZgHKQIDAQAB'
m = base64.b64decode(c)
m = hex(bytes_to_long(m))
print (m)
