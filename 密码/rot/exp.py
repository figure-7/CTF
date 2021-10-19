import hashlib

md5='38e4c352809e150186920aac37190cbc'
demo='flag{www_shiyanbar_com_is_very_good_'
for i in range(49,123):
    for j in range(49,123):
        for k in range(49,123):
            for l in range(49,123):
                demo = demo + chr(i) + chr(j) + chr(k) +chr(l) + '}'
                if hashlib.md5(demo.encode('utf8')).hexdigest() == md5:
                    print(demo)
                demo = demo[:-5]
