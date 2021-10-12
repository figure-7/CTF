import base64

if __name__ == '__main__':
    cur = 5
    res = ""
    ss = 'afZ_r9VYfScOeO_UL^RWUc'
    for letter in ss:
        res += chr(ord(letter) + cur)
        cur += 1
    print(res)
