
import base64
 
 
def strToBase64(s):
    '''
    将字符串转换为base64字符串
    :param s:
    :return:
    '''
    strEncode = base64.b64encode(s.encode('utf8'))
    return str(strEncode, encoding='utf8')
 
def base64ToStr(s):
    '''
    将base64字符串转换为字符串
    :param s:
    :return:
    '''
    strDecode = base64.b64decode(bytes(s, encoding="Latin1"))
    return str(strDecode, encoding='Latin1')
 
 
if __name__ == '__main__':
    s = "python:字符串转换成字节的三种方式"
    
    print(strToBase64(s))
    
    res = ""
    cur = 1
    s2 = 'Z25ka4A7O21AO3BERDtCSEp3QEhFSHpFe01LVUqDU1WFWlddXVhYXV2n'
    ss = base64ToStr(s2)
    print(ss)
    for letter in ss:
        res += chr(ord(letter) - cur)
        cur += 1
    print(res)
