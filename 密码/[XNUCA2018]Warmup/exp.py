from Crypto.Util.number import *

def egcd(a, b):
    if a == 0:
      return (b, 0, 1)
    else:
      g, y, x = egcd(b % a, a)
      return (g, x - (b // a) * y, y)
      
n=25118186052801903419891574512806521370646053661385577314262283167479853375867074736882903917202574957661470179148882538361560784362740207649620536746860883395110443930778132343642295247749797041449601967434690280754279589691669366595486824752597992245067619256368446164574344449914827664991591873150416287647528776014468498025993455819767004213726389160036077170973994848480739499052481386539293425983093644799960322581437734560001018025823047877932105216362961838959964371333287407071080250979421489210165485908404019927393053325809061787560294489911475978342741920115134298253806238766543518220987363050115050813263
e1=7669
c1=22917655888781915689291442748409371798632133107968171254672911561608350738343707972881819762532175014157796940212073777351362314385074785400758102594348355578275080626269137543136225022579321107199602856290254696227966436244618441350564667872879196269074433751811632437228139470723203848006803856868237706401868436321225656126491701750534688966280578771996021459620472731406728379628286405214996461164892486734170662556518782043881759918394674517409304629842710180023814702447187081112856416034885511215626693534876901484105593275741829434329109239483368867518384522955176807332437540578688867077569728548513876841471
e2=6947
c2=20494665879116666159961016125949070097530413770391893858215547229071116025581822729798313796823204861624912909030975450742122802775879194445232064367771036011021366123393917354134849911675307877324103834871288513274457941036453477034798647182106422619504345055259543675752998330786906376830335403339610903547255965127196315113331300512641046933227008101401416026809256813221480604662012101542846479052832128788279031727880750642499329041780372405567816904384164559191879422615238580181357183882111249939492668328771614509476229785062819586796660370798030562805224704497570446844131650030075004901216141893420140140568

s = egcd(e1, e2)
s1 = s[1]
s2 = s[2]
if s1<0:
   s1 = - s1
   c1 = inverse(c1, n)
elif s2<0:
   s2 = - s2
   c2 = inverse(c2, n)


m=(pow(c1,s1,n)*pow(c2,s2,n)) % n
print (long_to_bytes(m))
