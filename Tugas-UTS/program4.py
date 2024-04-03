# -------------------------------------------------------------------------
  # JUDUL  : PROGRAM PERHITUNGAN DIAMETER LINGKARAN
  # INPUT  : Angka "Masukkan diameter lingkaran (D):"
  # PROSES : Menghitung jari-jari lingkaran, Menghitung luas lingkaran (LL) 
  # 	       dan Menghitung keliling, dan Menghitung keliling lingkaran   
  #		 (KL)
  # OUTPUT : Menampilkan hasil dari Perhitungan jari-jari lingkaran,
  #		 Menghitung luas lingkaran (LL), dan Menghitung keliling
  #		 lingkaran (KL)
# -------------------------------------------------------------------------

import math

# ALGORITMA----------------------------------------------------------------

# Menerima input diameter dari pengguna
diameter = float(input("Masukkan diameter lingkaran (D): "))

# Menghitung jari-jari lingkaran
jari_jari = diameter / 2

# Menghitung luas lingkaran (LL)
luas_lingkaran = math.pi * jari_jari**2

# Menghitung keliling lingkaran (KL)
keliling_lingkaran = 2 * math.pi * jari_jari

# Menampilkan hasil perhitungan
print(f"Luas Lingkaran    : {luas_lingkaran}")
print(f"Keliling Lingkaran: {keliling_lingkaran}")

# -------------------------------------------------------------------------
