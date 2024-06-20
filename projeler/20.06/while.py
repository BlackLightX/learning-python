# sayilar = [4,6,9,10,35,57,89,125,244]

# i = 0

# while i < len(sayilar):
#     print(sayilar[i])
#     i += 1

# i = int(input("Başlangıç değeri giriniz: "))
# s = int(input("Bitiş değeri giriniz: "))

# while i < s:

#     if(i%2==1):
#         print(i)

#     i+=1


# i = 100

# while (i > 1):
#     print(i)
#     i -=1


sayilar = []
i=0

while (i<5):
    sayi = int(input("5 sayı giriniz: "))
    sayilar.append(sayi)
    i+=1
sayilar.sort()
print("Girilen sayılar: ",sayilar)
