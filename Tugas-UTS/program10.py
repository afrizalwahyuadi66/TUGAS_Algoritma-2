def main():
    # Menerima input dua bilangan bulat AWAL dan AKHIR dari pengguna
    AWAL = int(input("Masukkan bilangan AWAL: "))
    AKHIR = int(input("Masukkan bilangan AKHIR: "))

    # Periksa apakah AWAL lebih kecil dari AKHIR
    if AWAL >= AKHIR:
        print("AWAL harus kurang dari AKHIR.")
        return

    # Mencetak semua bilangan dari AWAL hingga AKHIR
    print("Deret bilangan dari", AWAL, "sampai", AKHIR, ":")
    for i in range(AWAL, AKHIR + 1):
        print(i)

if __name__ == "__main__":
    main()
