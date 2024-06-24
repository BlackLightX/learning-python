# 1- Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız. 

def kelimeTekrarla(tekrarSayisi, kelime):
    return tekrarSayisi * kelime

sonuc = kelimeTekrarla(5,"Merhaba\n")

print(sonuc)

####################################################################################

# 2- Dikdörgenin alan ve çevresini hesaplayan fonksiyonu yazınız.

def dikdortgenAlanCevre(kisaKenar, uzunKenar):
    print("Dikdörtgenin Alanı:",kisaKenar * uzunKenar)
    print("Dikdörtgenin Çevresi:",2 * (kisaKenar + uzunKenar))
   
dikdortgenAlanCevre(int(input("Kısa kenar: ")), int(input("Uzun kenar: ")))

####################################################################################

# 3- Yazı tura uygulamasını fonksiyon kullanarak yapınız. (Random modülü)

def yaziTura():
    import random
    uret = random.randint(0,1)
    if (uret == 1):
        print("Yazı")
    else:
        print("Tura")

yaziTura()

####################################################################################
# 4- Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız.

def asalSayi(sayi1, sayi2):

    for i in range(sayi1,sayi2+1):
        if(i>1):
            for j in range(2,i):
                if ((i % j) == 0 ):
                    break
            else:
                print(i)

asalSayi(int(input("1. Sayıyı giriniz: ")),int(input("2. Sayıyı giriniz: ")))

####################################################################################
# 5- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız.

def tamBolen(sayi):
    liste = []

    for i in range(1,sayi+1,1):
        if (sayi % i == 0):
            liste.append(i)
            
    print(f"{sayi} sayısının tam bölenleri: {liste}")
       
tamBolen(int(input("Sayı giriniz: ")))
