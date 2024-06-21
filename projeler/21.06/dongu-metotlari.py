# Hesap makinesi:

# for i in range(1,10,1):
#     print('------------')
#     for k in range(0,10,1):
#         print('{} * {} = {}'.format(i,k,i*k))


# Asal sayı kontrol uygulaması:

# Benim yaptığım

# sayi = int(input("Sayı giriniz: "))

# hesap = range(2,sayi,1)

# if (sayi == 1):
#     print("{sayi} Sayı asaldır: ",sayi)

# for i in hesap:
#     if (sayi % i == 0):
#         print("{sayi} Sayı asal değildir: ",sayi)
#         break
#     else:
#         print("{sayi} Sayı asaldır: ",sayi)
#         break


# Doğru olan

sayi = int(input("Sayı giriniz: "))

asalMi = True

if (sayi == 1):
    asalMi = True

for i in range(2,sayi):
    if (sayi % 1 == 0):
        asalMi = False
        break

if asalMi:
    print("Sayı asaldır.")

else:
    print("Sayı asal değildir.")
