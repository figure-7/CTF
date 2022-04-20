a = "abcdefghijklmnopqrstuvwxyz"
c = "0156 0821 1616 0041 0140 2130 1616 0793".split(" ")
N = 2537
e = 13
d = 937
p = 43
q = 59
phi_N = (p-1)*(q-1)

m = "".join(a[pow(int(i),d,N)] for i in c)
print (m)
