import requests
import json

# Altın fiyatlarını çekeceğimiz API adresi ve gerekli başlıklar
url = "https://api.collectapi.com/economy/goldPrice"
headers = {
    'content-type': "application/json",
    'authorization': "API_KEY_HERE"
}

# Gerçek API İsteği (Gerektiğinde yorumdan çıkarılabilir)
response = requests.get(url, headers=headers)
data = response.json()

portfoy = {
    "nakit" : 0,
    "Gram Altın" : 0,
    "Çeyrek Altın" : 0,
    "Yarım Altın" : 0,
    "Tam Altın" : 0,
}

print("\n----------------\n")

portfoy["nakit"] = int(input("Nakit Miktarı giriniz: "))

while True:
    print("\n----------------\n")
    print("1 Alım Yapmak")
    print("2 Satım Yapmak")
    print("3 Portföy Durumu")
    print("4 Çıkış Yapmak")

    secim = input("Yapmak istediğiniz işlemi seçiniz: (1-4)")

    print("\n----------------\n")

    if secim == "1":
        print("Alım İşlemi:")
        alinacak_altin = input("Alım Yapmak istediğiniz altın türü: ")
        alinacak_miktar = int(input("Alım Yapmak istediğiniz altın miktarı: "))


        for altin in data["result"]:
            if altin["name"] == alinacak_altin:
                fiyat = altin["selling"]  
                toplam_tutar = fiyat * alinacak_miktar
                
                if portfoy["nakit"] >= toplam_tutar:
                    portfoy["nakit"] -= toplam_tutar
                    portfoy[alinacak_altin] += alinacak_miktar
                    print(f"Alım başarılı! Tutar: {toplam_tutar} TL")
                else:
                    print("Bakiyeniz bu alım için yetersiz.")
        
    elif secim == "2":
        print("Satım İşlemi:")
        satilacak_altin = input("Satım Yapmak istediğiniz altın türü: ")
        satilacak_miktar = int(input("Satım Yapmak istediğiniz altın miktarı: "))

        if portfoy[satilacak_altin] < satilacak_miktar:
            print("Satım yapılacak altın türü mevcut portföyde bulunmuyor.")
        else:
            for altin in data["result"]:
                if altin["name"] == satilacak_altin:
                    fiyat = altin["buying"]
                    toplam_tutar = fiyat * satilacak_miktar
                    portfoy[satilacak_altin] -= satilacak_miktar
                    portfoy["nakit"] += toplam_tutar
                    print(f"Satım başarılı! Tutar: {toplam_tutar} TL")
        
    elif secim == "3":
        print("Portföy Durumu:")
        print(f"Nakit: {portfoy['nakit']} TL")
        for altin in data["result"]:
            if altin["name"] in portfoy:
                print(f"{altin['name']}: {portfoy[altin['name']]} Adet x {altin['selling']} TL = {portfoy[altin['name']] * altin['selling']} TL")

    elif secim == "4":
        print("Çıkış Yapılıyor...")
        break

    else:
        print("Geçersiz bir seçim yaptınız.")
