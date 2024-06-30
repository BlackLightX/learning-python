# Lambda fonksiyonu

sonuc = (lambda a : a**5) (2)
print(sonuc)


deneme = lambda c : c**3
sonuc2 = deneme(2)
print(sonuc2)


tersCevir = lambda d : d[::-1]
sonuc3 = tersCevir("Merhaba")
print(sonuc3)


def fonk(f):
    return lambda k : f * k

sonuc4 = fonk(5)
print(sonuc4)
sonuc5 = sonuc4(3)
print(sonuc5)


# Map fonksiyonu

sayilar = [1,-2,5,-7,-9]
str_sayilar = ["1","2","5","7","9"]
isimler = ["ali","deniz","emel","Çınar"]
kullanicilar = [
    {"ad": "ali", "soyad":"Yılmaz"},
    {"ad": "ahmet", "soyad":"Yılmaz"}
]

sonuc6 = list(map(str.capitalize,isimler))
print(sonuc6)

sonuc7 = list(map(len,isimler))
print(sonuc7)

sonuc8 = list(map(lambda x: abs(x*3),sayilar))
print(sonuc8)

sonuc9 = list(map(lambda x: x["ad"],kullanicilar))
print(sonuc9)


# Filter fonksiyonu

liste = [5,15,3,20,115,24,100,243,7,1,27,33]

def tekSayi(n):
    return n % 2 == 1

sonuc10 = list(filter(tekSayi,liste))
print(sonuc10)

sonuc11 = list(filter(lambda c : c[1]=="l",isimler))
print(sonuc11)
