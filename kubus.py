#gambar kubus
def gambar_kubus():
    print("""
      +------+
     /      /|
    +------+ |
    |      | +
    |      |/
    +------+
    """)

#rumus kubus
def hitung_kubus(r):
    luas = 6 * r * r
    volume = r * r * r
    return luas, volume