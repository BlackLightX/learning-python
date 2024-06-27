#bankamatik para cekme örneği

hesapA = {
    "ad" : "Ahmet Yılmaz",
    "hesapNo" : "123456",
    "bakiye" : 3000,
    "ekHesap" : 2000
}

hesapB = {
    "ad" : "Mehmet Özdemir",
    "hesapNo" : "654321",
    "bakiye" : 6000,
    "ekHesap" : 3000
}

def paraCek (hesap,miktar):
    print(f"Merhaba {hesap['ad']}")
    toplam = hesap["bakiye"] + hesap["ekHesap"]

    if (hesap["bakiye"] >= miktar):
        hesap["bakiye"] -= miktar
        return hesap["bakiye"]
    
    elif (hesap["bakiye"] < miktar):
        if toplam >= miktar:
            kullanim = input("Hesabınızdaki para yetersiz. Ek hesap kullanılsın mı? E/H ")
            
            if (kullanim == "E"):       
                ekHesapKullanimi = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekHesap"] -= ekHesapKullanimi
                return hesap["bakiye"], hesap["ekHesap"]      
            else:
                return "Ek hesabınızı kullanmadığınız için bakiye yetersiz."    
        else:
            return "Ek hesapta yeteri kadar bakiye yok."
    else:
        return "Toplam  bakiye yetersiz."

    

sonuc = paraCek(hesapB,7000)
print(sonuc)

print(hesapB)

# global ve local değişken tanımlama örneği

ad = 'Ahmet'

def isimDegis(isim):

    global ad
    ad = isim
    print(ad)

isimDegis('Mehmet')
print(ad)

