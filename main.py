def hitung_luas_persegi(sisi):
    print(f"Menghitung luas persegi dengan sisi {sisi}...")
    return sisi * sisi

def hitung_volume_persegi(sisi):
    print(f"Menghitung volume persegi dengan sisi {sisi}...")
    return sisi**3

def hitung_luas_segitiga(alas, tinggi):
    print(f"Menghitung volume persegi dengan alas: {alas} dan tinggi: {tinggi}")
    return (0.5)*alas*tinggi

def main():
    print("Selamat datang di Kalkulator Bangun Datar!")
    hitung_persegi = hitung_luas_persegi(4)
    print(hitung_persegi)
    print(hitung_volume_persegi(4))
    print(hitung_luas_segitiga(10, 5))

if __name__ == "__main__":
    main()
