# sayi1 = int(input('1. Sayi: '))
# sayi2 = int(input('2. Sayi: '))

# sonuc = sayi1 > sayi2
# print(f"Sayi 1 {sayi1}, Sayi 2 {sayi2} den büyüktür: {sonuc}")


# sayi = int(input("Sayı: "))

# sonuc = (sayi % 2) == 0

# print(f"Girilen sayı {sayi} sonuç 1 ise çift sayı, 0 ise tek sayıdır Sonuç: {int(sonuc)}")


# vize1 = float(input("1. Vize notu: "))
# vize2 = float(input("2. Vize notu: "))
# final = float(input("Final notu: "))

# vizenotu = ((vize1+vize2) / 2) * 0.6
# finalnotu = final * 0.4
# ortalama = vizenotu + finalnotu

# print(f"Ortalama: {ortalama} ve dersten geçme durumu: {ortalama>=50}")

mail = "asd123@gmail.com"
sifre = "asd123"

e_mail = input("Mail adresini giriniz: ")
parola = input("Şifrenizi giriniz: ")


mailDogrulama = (e_mail.lower().strip() == mail)

sifreDogrulama = (parola.lower().strip() == sifre)

print(f"Mail doğruluğu {mailDogrulama}, Parola doğruluğu {sifreDogrulama}")
