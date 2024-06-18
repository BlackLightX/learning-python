# x = int(input("Sayi Gir: "))

# if (x>50) and  (x<100):
#     print("Sayi 50 ile 100 arasındadır. Sayı: ",x)

# else:
#     print("Sayi 50 ile 100 arasında değildir. Sayı: ",x)


# x = int(input("x: "))
# y = int(input("y: "))
# z = int(input("z: "))

# if (x > y) and (x > z):
#     print(f"{x} en büyük sayıdır.")
# elif (y > z) and (y > x):
#     print(f"{y} en büyük sayıdır.")
# else:
#     print(f"{z} en büyük sayıdır.")



#Yakıt tüketim uygulaması

benzinFiyat = 40.50
dizelFiyat = 40.84

yakitTuketimOrtalamasi = float(input("100 km deki ortalama yakıt tüketimi: "))
gidilenYol = float(input("Gidilen yol (km): "))
yakitTipi = input("Yakıt tipiniz nedir :")

toplamTuketim = (gidilenYol * (yakitTuketimOrtalamasi / 100 )) #km'deki yakit tüketimi

if(yakitTipi == "benzin"):
    toplamUcret = benzinFiyat * toplamTuketim
    print("Tüketiminize göre ücretiniz: ",toplamUcret)


elif(yakitTipi == "dizel"):
    toplamUcret = dizelFiyat * toplamTuketim
    print("Tüketiminize göre ücretiniz: ",toplamUcret)

else:
    print("Yanlış yakıt tipi. dizel/benzin")
