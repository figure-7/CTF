str = 'ComeChina'   #密文字符串
for temp in str:
    if(ord(temp) + 13 > ord('z')):
        print(chr(ord(temp) + 13 - 26), end = '')   #如果超出z，减26使其回到A-z范围内
    else:
        print(chr(ord(temp) + 13), end = '')
print('')
