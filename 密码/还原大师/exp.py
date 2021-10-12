import hashlib
s = 'TASC?O3RJMV?WDJKX?ZM' #分别遍历所有大写字符组合替换?字符得到
for i in range(26):
    temp1 = s.replace('?', str(chr(65 + i)), 1)
    for j in range(26):
        temp2 = temp1.replace('?', str(chr(65 + j)), 1)
        for k in range(26):
            temp3 = temp2.replace('?', str(chr(65 + k)), 1)
            res = hashlib.md5(temp3.encode('utf-8')).hexdigest().upper()
            #if s[:4] == 'E903':
            print (res)
