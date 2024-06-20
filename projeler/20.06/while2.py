#    Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
#    ** ürün sayısını kullanıcıya sorun.
#    ** dictionary listesi yapısı (urunAdi, fiyat) şeklinde olsun.
#    ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.

urunSayisi = int(input("Ürün sayısını giriniz: "))

i = 0
urunler = []

while i < urunSayisi:
    urunAd = input("Ürün adini giriniz: ")
    urunFiyat = input("Ürün fiyatını giriniz: ")
    urunler.append({
        "Ürün Adı" : urunAd,
        "Ürün Fiyatı" : urunFiyat
    })
    i +=1

print("\n",urunler)


for urun in urunler:
    print(f"\nÜrün adı: {urun['Ürün Adı']} ve Ürün fiyatı: {urun['Ürün Fiyatı']} TL")

# Kendime not:
# Prefix hataları yapıyorum. {} ve [] işaretlerini koyacağım yerleri karıştırıyorum. 
# List ve Dict kavramını karıştırıyorum. Buna tekrar bakmam gerek.
# List ve dict'in metotlarını Google'dan bakarak kullanmaya çalışıyorum. Bu kısmada tekrar bakmam gerek.
