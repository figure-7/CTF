s = 'XMZFSLDZ' #这里写用来实现凯撒的字符串
str = s.lower()
num = 1
for i in range(26):
    print("{:<2d}".format(num), end = '')
    for temp in str:
        if(ord(temp) + num > ord('z')):
            print(chr(ord(temp) + num - 26), end = '')
        else:
            print(chr(ord(temp) + num), end = '')
    num += 1
    print('')
