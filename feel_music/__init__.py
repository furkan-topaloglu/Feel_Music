"""
Feel Music paketi
------------------

Kişisel mini Spotify Wrapped fikrinden esinlenmiş, ruh haline göre
şarkı önerisi yapan basit bir Python uygulaması.

Ana bileşenler:
- data.py        : Şarkı veritabanı
- mood_engine.py : Ruh haline göre şarkı seçme mantığı
- player.py      : Spotify bağlantısını açma
- gui.py         : Tkinter ile basit grafik arayüz
"""

__all__ = [
    "data",
    "mood_engine",
    "player",
    "gui",
]


