# -------------------------------------------------------------------------
  # JUDUL  : PROGRAM PERHITUNGAN SEGITIGA SAMA SISI
  # INPUT  : Kata “Masukkan panjang sisi siku-siku X:”
  #		      “Masukkan panjang sisi siku-siku Y:”
  # PROSES : Menghitung luas segitiga siku-siku (LSS) dan Menghitung 	   
  #	       keliling segitiga siku-siku (KSS)
  # OUTPUT : Menampilkan hasil dari Luas Segitiga Siku-siku (KSS) dan 	    
  #	       Keliling segitiga Siku-siku (KSS)
# -------------------------------------------------------------------------

# ALGORITMA----------------------------------------------------------------

# Menerima input panjang sisi siku-siku X dan Y dari pengguna
panjang_sisi_x = float(input("Masukkan panjang sisi siku-siku X: "))
panjang_sisi_y = float(input("Masukkan panjang sisi siku-siku Y: "))

# Menghitung luas segitiga siku-siku (LSS)
luas_segitiga_siku = 0.5 * panjang_sisi_x * panjang_sisi_y

# Menghitung panjang sisi miring (hypotenuse)
panjang_miring = (panjang_sisi_x**2 + panjang_sisi_y**2)**0.5

# Menghitung keliling segitiga siku-siku (KSS)
keliling_segitiga_siku = panjang_sisi_x + panjang_sisi_y + panjang_miring

# Menampilkan hasil perhitungan
print(f"Luas Segitiga Siku-Siku    : {luas_segitiga_siku}")
print(f"Keliling Segitiga Siku-Siku: {keliling_segitiga_siku}")

# -------------------------------------------------------------------------
