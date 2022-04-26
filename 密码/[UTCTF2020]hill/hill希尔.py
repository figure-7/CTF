s='wznqcaduqopfkqnwofDbzgeu'
flag_pre='utflag'
def getit(a1,b1,c1,a2,b2,c2,a3,b3,c3):
    for i in range(26):
        for j in range(26):
            if (a1 * i + b1 * j) % 26 == c1 and (a2 * i + b2 * j) % 26 == c2 and (a3 * i+b3*j) % 26 == c3:
                return (i,j)
x1=getit(22,25,20,13,16,5,2,0,0)
x2=getit(22,25,19,13,16,11,2,0,6)
#n=2对应上面x1中wz u,nq f,ca a（也就是wznqca两位区分,utflag每位分别追加在x1和x2中）和x2中wz t,nq l,ca g
import string
flag=''
for i in range(0, len(s),2):
    flag+=string.ascii_letters[(x1[0]*string.ascii_letters.index(s[i])+x1[1]*string.ascii_letters.index(s[i+1]))%26]
    flag+=string.ascii_letters[(x2[0]*string.ascii_letters.index(s[i])+x2[1]*string.ascii_letters.index(s[i+1]))%26]
print(flag)

#utflagdngeruscphertextqq
