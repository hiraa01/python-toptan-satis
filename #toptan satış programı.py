#toptan satış programı
#kullanıcının aldığı paket sayısına göre ödeyeceği tutarı gösteren program
# 100 paket ve üzerinde paket başına 10 tl
# 61-99 paket arasında paket başı 12 tl
# 30-60  15 tl
# 1-29 20 tl olmaktadır.
while True:
    x= int(input("lütfen kaç paket almak istediğinizi giriniz: "))
    if x<=29 and x>1:
        print("ödeyeceğiniz tutar: ", x*20)
    elif x<=60 and x>=30:
        print("ödeyeceğiniz tutar: ", x*15)
    elif x<=99 and x>=61:
        print("ödeyeceğiniz tutar: ", x*12)
    elif x>=100:
        print("ödeyeceğiniz tutar: ", x*10)
    else:
        print("geçersiz giriş.")
#hocanın yazdığı...

while True:
    p= int(input("lütfen kaç paket almak istediğinizi giriniz: "))    
    t= None #herhangi bir değer tanımlamadığımız ilerde tanımlayabileceğimız zaman none kullanırız
    if p>=100:
        t= p*10
    elif p>60:
        t= p*12
    elif p>=30:
        t= p*15
    elif p>=1:
        t= p*20
    else: 
        print("lütfen 0 dan büyük bir sayı giriniz.")
    if t is not None: 
        print("ödemeniz gereken tutar: {}".format(t)) 
    elif p>0:
        print("ödemeniz gereken tutar bulunmamaktadır.")
