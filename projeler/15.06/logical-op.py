# sayi = int(input("Sayı giriniz: "))

# kontrol = 50 < sayi < 100

# kontrol2 = (sayi > 50) and (sayi < 100)

# print(kontrol, kontrol2)


# sonuc = (sayi > 0) and ((sayi % 2) == 1)

# print("Sonuc tek sayi mi ?",sonuc)


# a = int(input("a sayısını giriniz: "))

# b = int(input("b sayısını giriniz: "))

# c = int(input("c sayısını giriniz: "))

# sonuc = (a > b) and (a > c)

# sonuc = (b > a) and (b > c)

# sonuc = (c > a) and (c > b)


ad = input("Ad: ")
kg = float(input("Kilo: "))
boy = float(input("Boy: "))

formul = kg / (boy ** 2)

zayif = (formul >= 0) and (formul <= 18.4)

normal = (formul >= 18.5) and (formul <= 24.9)

fazlaKilo = (formul >= 25.0) and (formul <= 29.9)

sisman = (formul >= 30.0) and (formul <= 34.9)

print(f"{ad} kilo indeksi göre {zayif} ,kilo indeksi : {formul}")
print(f"{ad} kilo indeksi göre {normal} ,kilo indeksi : {formul}")
print(f"{ad} kilo indeksi göre {fazlaKilo} ,kilo indeksi : {formul}")
print(f"{ad} kilo indeksi göre {sisman} ,kilo indeksi : {formul}")