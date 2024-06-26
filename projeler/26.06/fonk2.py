# Kendisine gönderilen 2 sayıdan hangisi büyük bulan fonksiyonu yazınız.

def sayiGonder(a,b):
    if(a>b):
        print(a)
    else:
        print(b)

sayiGonder(int(input("1.sayı: ")),int(input("2.sayı: ")))

# Kendisine gönderilen list, command, position ve value bilgilerine göre liste üzerinde güncelleme yapınız.
  # [1,2,3], ("add, remove"), ("beginning | end"), value 
  # list_operation([1,2,3],"add","end","4") => [1,2,3,4]
  # list_operation([1,2,3],"remove","beginning") => [2,3]

def guncelleme(liste, command, position, value=None):

    if (command == "add"):
        if(position == "beginning"):
            liste.insert(0,value)
            return liste
        elif(position == "end"):
            liste.append(value)
            return liste
    elif (command == "remove"):
        if(position == "beginning"):
            liste.pop(0)
            return liste
        elif(position == "end"):
            liste.pop(-1)
            return liste



sonuc = guncelleme([1,2,3], "add", "end",6)

print(sonuc)
