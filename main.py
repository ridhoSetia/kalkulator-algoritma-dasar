def hitung_luas_persegi(sisi):
    print(f"Menghitung luas persegi dengan sisi {sisi}...")
    return sisi * sisi

def main():
    print("Selamat datang di Kalkulator Bangun Datar!")
    hitung_persegi = hitung_luas_persegi(4)
    print(hitung_persegi)

if __name__ == "__main__":
    main()