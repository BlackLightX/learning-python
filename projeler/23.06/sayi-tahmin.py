# Sayı tahmin uygulaması 1

import random

sayiUret = random.randint(1,100)

print("Üretilen sayı:",sayiUret)

varsayilanHak = 5
sayac = 1

while (sayac <= varsayilanHak):
    sayiAl = int(input("1 ile 100 arasında bir sayı giriniz:"))
    if(sayiAl >= 1 and sayiAl <= 100):
        if(sayiUret == sayiAl):
            print("{0}. Tahmininiz doğru. {1}".format(sayac, sayiAl))
            break
        elif(sayiAl > sayiUret):
            print("Girilen sayıdan daha küçük bir sayı giriniz.")
        elif(sayiAl < sayiUret):
            print("Girilen sayıdan daha büyük bir sayı giriniz.")
        print(f"Kalan tahmin hakkınız: {varsayilanHak-sayac}")
        sayac +=1
    else:
        print("Girilen sayı 1 ile 100 arasında değildir.")

kullanılanHak = sayac-1

puan = 100 - (kullanılanHak * 20)

print(f"100 üzerinden alınan puan: {puan}")

if (sayac > varsayilanHak):
    print("Tahmin hakkınız bitti. 0 puan aldınız.")
