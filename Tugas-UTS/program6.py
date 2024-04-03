# -------------------------------------------------------------------------
 # JUDUL  : PROGRAM KATEGORI ANGKA (GANJIL,GENAP,NEGATIF,POSITIF,NOL)
 # INPUT  : Angka "Masukkan sebuah bilangan integer (X): "
 # PROSES : Menganalisa apakah angka yang kita input negatif atau positf 
 #	      dan Genap atau Ganjil atau nol
 # OUTPUT : "Analisis Bilangan: {kategori	} 
# -------------------------------------------------------------------------

# ALGORITMA----------------------------------------------------------------

# Menerima input bilangan integer dari pengguna
X = int(input("Masukkan sebuah bilangan integer (X): "))

# Analisis kategori bilangan
if X > 0 and X % 2 == 0:
    kategori = "Bilangan Genap Positif"
elif X < 0 and X % 2 == 0:
    kategori = "Bilangan Genap Negatif"
elif X > 0 and X % 2 != 0:
    kategori = "Bilangan Ganjil Positif"
elif X < 0 and X % 2 != 0:
    kategori = "Bilangan Ganjil Negatif"
else:
    kategori = "Nol"

# Menampilkan hasil analisis
print(f"")
print(f"==================Hasil==================")
print(f"Analisis Bilangan: {kategori}")

# -------------------------------------------------------------------------
