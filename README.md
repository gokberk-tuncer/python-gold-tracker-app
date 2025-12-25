# Python Gold Tracker App

🏆 **Python Gold Tracker App**, altın alım-satım işlemlerini takip etmenizi sağlayan, gerçek zamanlı altın fiyatlarını kullanan bir portföy yönetim uygulamasıdır.

## 📋 İçindekiler

- [Özellikler](#-özellikler)
- [Kurulum](#-kurulum)
- [Kullanım](#-kullanım)
- [API Yapılandırması](#-api-yapılandırması)
- [Desteklenen Altın Türleri](#-desteklenen-altın-türleri)
- [Örnek Kullanım](#-örnek-kullanım)
- [Gereksinimler](#-gereksinimler)
- [Katkıda Bulunma](#-katkıda-bulunma)
- [Lisans](#-lisans)

## ✨ Özellikler

- 💰 **Gerçek Zamanlı Altın Fiyatları**: CollectAPI üzerinden güncel altın fiyatlarını çeker
- 🛒 **Altın Alım İşlemleri**: Farklı altın türlerinde alım yapabilme
- 💵 **Altın Satım İşlemleri**: Portföyünüzdeki altınları satabilme
- 📊 **Portföy Takibi**: Anlık portföy durumunuzu görüntüleme
- 💳 **Nakit Yönetimi**: Bakiye kontrolü ve otomatik hesaplama
- 🔄 **Dinamik Fiyatlandırma**: Alış ve satış fiyatlarını ayrı ayrı hesaplama

## 🚀 Kurulum

### Gereksinimler

- Python 3.6 veya üzeri
- `requests` kütüphanesi

### Adımlar

1. **Projeyi klonlayın:**
```bash
git clone https://github.com/kullaniciadi/python-gold-tracker-app.git
cd python-gold-tracker-app
```

2. **Gerekli kütüphaneleri yükleyin:**
```bash
pip install requests
```

3. **API anahtarınızı yapılandırın:**
   - [CollectAPI](https://collectapi.com/) üzerinden ücretsiz bir hesap oluşturun
   - Gold Price API için API anahtarı alın
   - `main.py` dosyasındaki `API_KEY_HERE` kısmını kendi API anahtarınızla değiştirin

## 📖 Kullanım

Uygulamayı başlatmak için:

```bash
python main.py
```

### Ana Menü Seçenekleri

Program başladığında size aşağıdaki seçenekler sunulur:

1. **Alım Yapmak**: Nakit paranızla altın satın alın
2. **Satım Yapmak**: Portföyünüzdeki altınları satın
3. **Portföy Durumu**: Mevcut portföyünüzü ve değerini görüntüleyin
4. **Çıkış Yapmak**: Programdan çıkın

## 🔑 API Yapılandırması

`main.py` dosyasında API yapılandırması:

```python
url = "https://api.collectapi.com/economy/goldPrice"
headers = {
    'content-type': "application/json",
    'authorization': "YOUR_API_KEY_HERE"  # Buraya kendi API anahtarınızı girin
}
```

### API Anahtarı Alma

1. [CollectAPI](https://collectapi.com/) adresine gidin
2. Ücretsiz hesap oluşturun
3. Dashboard'dan "Gold Price" API'sini bulun
4. API anahtarınızı kopyalayın
5. `main.py` dosyasındaki `API_KEY_HERE` yerine yapıştırın

## 🥇 Desteklenen Altın Türleri

Uygulama aşağıdaki altın türlerini destekler:

- **Gram Altın**: 1 gram altın
- **Çeyrek Altın**: Çeyrek altın
- **Yarım Altın**: Yarım altın
- **Tam Altın**: Tam altın (Cumhuriyet altını)

## 💡 Örnek Kullanım

### Başlangıç

```
----------------
Nakit Miktarı giriniz: 10000
```

### Altın Alımı

```
----------------
1 Alım Yapmak
2 Satım Yapmak
3 Portföy Durumu
4 Çıkış Yapmak
Yapmak istediğiniz işlemi seçiniz: (1-4) 1

----------------
Alım İşlemi:
Alım Yapmak istediğiniz altın türü: Gram Altın
Alım Yapmak istediğiniz altın miktarı: 5
Alım başarılı! Tutar: 3250.50 TL
```

### Portföy Görüntüleme

```
Yapmak istediğiniz işlemi seçiniz: (1-4) 3

----------------
Portföy Durumu:
Nakit: 6749.50 TL
Gram Altın: 5 Adet x 650.10 TL = 3250.50 TL
Çeyrek Altın: 0 Adet x 1050.00 TL = 0 TL
Yarım Altın: 0 Adet x 2100.00 TL = 0 TL
Tam Altın: 0 Adet x 4200.00 TL = 0 TL
```

### Altın Satımı

```
Yapmak istediğiniz işlemi seçiniz: (1-4) 2

----------------
Satım İşlemi:
Satım Yapmak istediğiniz altın türü: Gram Altın
Satım Yapmak istediğiniz altın miktarı: 2
Satım başarılı! Tutar: 1298.00 TL
```

## 🎯 Özellikler ve İşlevler

### Alım İşlemi
- Gerçek zamanlı satış fiyatı kullanılır
- Bakiye kontrolü yapılır
- Yetersiz bakiye durumunda uyarı verilir
- Başarılı alımda portföy otomatik güncellenir

### Satım İşlemi
- Gerçek zamanlı alış fiyatı kullanılır
- Portföyde yeterli altın kontrolü yapılır
- Başarılı satımda nakit bakiye güncellenir

### Portföy Yönetimi
- Tüm altın türlerinin anlık değeri hesaplanır
- Nakit bakiye görüntülenir
- Her altın türü için adet ve toplam değer gösterilir
