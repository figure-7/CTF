from Crypto.Util.number import *
from gmpy2 import *
from functools import reduce
import sympy
import itertools
def My_base64_decode(inputs,s):
	bin_str = []
	for i in inputs:
		if i != '=':
			x = str(bin(s.index(i))).replace('0b', '')
			bin_str.append('{:0>6}'.format(x))
	outputs = ""
	nums = inputs.count('=')
	while bin_str:
		temp_list = bin_str[:4]
		temp_str = "".join(temp_list)
		if(len(temp_str) % 8 != 0):
			temp_str = temp_str[0:-1 * nums * 2]
		for i in range(0,int(len(temp_str) / 8)):
			outputs += chr(int(temp_str[i*8:(i+1)*8],2))
		bin_str = bin_str[4:]	
	print("Decrypted String:\n%s "%outputs)
h=['j','u','3','4']
h1=list(itertools.permutations(h,4))
for i in h1:
	m="".join(i)
	s = "JASGBWcQPRXEFLbCDIlmnHUVKTYZdMovwipatNOefghq56rs"+m+"kxyz012789+/"
	input_str="MyLkTaP3FaA7KOWjTmKkVjWjVzKjdeNvTnAjoH9iZOIvTeHbvD=="
	My_base64_decode(input_str,s)
