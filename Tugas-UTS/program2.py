# -------------------------------------------------------------------------
 # JUDUL  : PROGRAM PERHITUNGAN SEGITIGA SAMA SISI
 # INPUT  : Angka “Masukkan panjang sisi segitiga sama sisi (S):”
 # PROSES : Menghitung luas segitiga (LS) dan Menghitung keliling segitiga
 #          (KS)
 # OUTPUT : Menampilkan hasil dari Luas Segitiga (LS) dan Keliling segitiga   
 #	      (KS)
 #-------------------------------------------------------------------------

#ALGORITMA-----------------------------------------------------------------

# Menerima input panjang sisi dari pengguna
panjang_sisi = float(input("Masukkan panjang sisi segitiga sama sisi (S): "))

# Menghitung luas segitiga (LS)
luas_segitiga = (panjang_sisi**2 * (3**0.5)) / 4

# Menghitung keliling segitiga (KS)
keliling_segitiga = 3 * panjang_sisi

# Menampilkan hasil perhitungan
print(f"Luas Segitiga    : {luas_segitiga}")
print(f"Keliling Segitiga: {keliling_segitiga}")

#--------------------------------------------------------------------------
