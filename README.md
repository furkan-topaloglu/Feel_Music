## Feel Music – Ruh Haline Göre Spotify Şarkı Önerici

Bu mini proje, Spotify Wrapped'in ilhamıyla kendi dinleme zevkine göre hazırlanmış basit bir **ruh hali tabanlı şarkı öneri uygulaması**dır.

Uygulama şu sanatçılardan şarkılar seçer:

- Tan Taşçı
- Ebru Gündeş
- Tan Taşçı Başkanlar Korosu
- Sibel Can

Sen sadece **“Bugün ruh halin nasıl?”** sorusuna cevap verirsin, uygulama da ruh haline göre uygun bir şarkı seçip Spotify bağlantısını açar.

Özellikler:

- Basit grafik arayüz (GUI, `tkinter` ile)
- Modüler Python kod yapısı (CV ve GitHub için okunabilir)
- Harici kütüphane gerektirmez (sadece Python standart kütüphaneleri)

---

### Kurulum

Depoyu klonladıktan veya klasörü indirdikten sonra:

```bash
cd feel_music
python -m venv venv
venv\Scripts\activate  # Windows için
pip install -r requirements.txt
```

Bu projede harici bağımlılık yok, `requirements.txt` dosyası dokümantasyon amaçlıdır.

---

### Çalıştırma (GUI)

```bash
python -m feel_music.gui
```

Küçük bir pencere açılır, butonlardan ruh halini seçersin:

- Mutlu / Enerjik
- Hüzünlü
- Sakin
- Sürpriz

Seçimden sonra şarkı bilgisi ekranda gösterilir ve Spotify bağlantısı tarayıcıda açılır.

---

### Proje Yapısı

```text
feel_music/
├─ feel_music/
│  ├─ __init__.py
│  ├─ data.py         # Şarkı veritabanı ve sanatçı listesi
│  ├─ mood_engine.py  # Ruh haline göre şarkı filtreleme ve seçim mantığı
│  ├─ player.py       # Spotify bağlantısını açma (tarayıcı)
│  └─ gui.py          # Tkinter ile basit grafik arayüz
├─ requirements.txt
└─ README.md
```

---

### Geliştirme Fikirleri

- Kullanıcıdan favori şarkıları alıp veritabanını genişletmek
- Daha fazla ruh hali eklemek (öfke, nostalji, odaklanma vb.)
- Spotify API ile doğrudan kullanıcının hesabında playlist oluşturmak
- Şarkı geçmişini (history) bir JSON dosyasında tutmak

Bu haliyle proje, hem **kişisel bir mini Wrapped** fikrini gösteriyor hem de **Python ile modüler, okunabilir bir uygulama tasarlama** becerisini sergiliyor; bu yüzden GitHub ve CV için uygundur.
