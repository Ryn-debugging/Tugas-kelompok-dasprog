import math

def gambar_limas():
    print("""
        /\\
       /  \\
      / /\\ \\
     / /  \\ \\
    /_/____\\_\\
    """)

def hitung_limas(sisi_alas, tinggi_limas):
    luas_alas = sisi_alas * sisi_alas
    tinggi_sisi_tegak = math.sqrt((0.5 * sisi_alas) ** 2 + tinggi_limas ** 2)
    luas_selimut = 4 * (0.5 * sisi_alas * tinggi_sisi_tegak)
    luas = luas_alas + luas_selimut
    volume = (1 / 3) * luas_alas * tinggi_limas
    return luas, volume

def gambar_tabung():
    print("""
      .------.
     (        )

     |`------'|
     |        |
     |        |
     `.______.'
    """)

def hitung_tabung(r, t):
    luas = 2 * math.pi * r * (r + t)
    volume = math.pi * (r ** 2) * t
    return luas, volume
  
