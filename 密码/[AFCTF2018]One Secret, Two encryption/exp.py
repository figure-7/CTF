n1=4850297138162223468826481623082440249579136876798312652735204698689613969008632545220976699170308454082390834742570718247804202060929493571642074679428565168405877110681518105667301785653517697684490982375078989886040451115082120928982588380914609273008153977907950532498605486225883973643141516024058315360572988744607134110254489421516026937249163493982681336628726033489124705657217768229058487155865265080427488028921879608338898933540825564889012166181346177276639828346376362168934208822467295673761876965864573164529336885250577357767314256581019474130651412100897839606491189424373959244023695669653213498329
n2=2367536768672000959668181171787295271898789288397672997134843418932405959946739637368044420319861797856771490573443003520137149324080217971836780570522258661419034481514883068092752166752967879497095564732505614751532330408675056285275354250157955321457579006360393218327164804951384290041956551855334492796719901818165788902547584563455747941517296875697241841177219635024461395596117584194226134777078874543699117761893699634303571421106917894215078938885999963580586824497040073241055890328794310025879014294051230590716562942538031883965317397728271589759718376073414632026801806560862906691989093298478752580277
import gmpy2
print(gmpy2.gcd(n1,n2))
p11=174410123761631337520799179808598127914184971978811796722414215239874114048347830609255805203105210941441708658356189056418366104015120153227123562166980882513945308613658062284844636341082646995916907680076101741743945938845994542592182491688095893467336553001430454260431413695816790105384153941685561590503
p12=n1//p11
p21=174410123761631337520799179808598127914184971978811796722414215239874114048347830609255805203105210941441708658356189056418366104015120153227123562166980882513945308613658062284844636341082646995916907680076101741743945938845994542592182491688095893467336553001430454260431413695816790105384153941685561590503
p22=n2//p21
e1=1666626632960368239001159408047765991270250042206244157447171188195657302933019501932101777999510001235736338843107709871785906749393004257614129802061081155861433722380145001537181142613515290138835765236002811689986472280762408157176437503021753061588746520433720734608953639111558556930490721517579994493088551013050835690019772600744317398218183883402192060480979979456469937863257781362521184578142129444122428832106721725409309113975986436241662107879085361014650716439042856013203440242834878648506244428367706708431121109714505981728529818874621868624754285069693368779495316600601299037277003994790396589299
e2=65537
import rsa
#下面的也可以用e1,p11,p12,n1,flag_encry1解
d1=int(gmpy2.invert(e2,(p21-1)*(p22-1)))
Rsa=rsa.PrivateKey(n2,e2,d1,p21,p22)
with open('flag_encry2','rb') as f:
     cipher1=f.read()
     print(rsa.decrypt(cipher1,Rsa))

