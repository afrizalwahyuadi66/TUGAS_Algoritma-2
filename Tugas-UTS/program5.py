# -------------------------------------------------------------------------
  # JUDUL  : PROGRAM PERHITUNGAN JARAK TEMPUH
  # INPUT  : Angka	"Masukkan kecepatan pertama (V1): "
  #		     		"Masukkan kecepatan kedua (V2): "
  #				"Masukkan kecepatan ketiga (V3): "
  #				"Masukkan waktu tempuh pertama (T1): "
  #				"Masukkan waktu tempuh kedua (T2): "
  #				"Masukkan waktu tempuh ketiga (T3): "
  # PROSES : Menghitung jarak tempuh (S1, S2, S3), Menghitung luas 
  #    	 lingkaran (LL) Menghitung rata-rata jarak tempuh (Rata_jarak)
  # OUTPUT : Menampilkan hasil perhitungan jarak tempuh (S1, S2, S3),
  #		 Menghitung luas lingkaran (LL) Menghitung rata-rata jarak           
  #		 tempuh (Rata_jarak)
# -------------------------------------------------------------------------

# ALGORITMA----------------------------------------------------------------

# Menerima input kecepatan (V1, V2, V3) dari pengguna
kecepatan1 = float(input("Masukkan kecepatan pertama (V1): "))
kecepatan2 = float(input("Masukkan kecepatan kedua (V2): "))
kecepatan3 = float(input("Masukkan kecepatan ketiga (V3): "))

# Menerima input waktu tempuh (T1, T2, T3) dari pengguna
waktu_tempuh1 = float(input("Masukkan waktu tempuh pertama (T1): "))
waktu_tempuh2 = float(input("Masukkan waktu tempuh kedua (T2): "))
waktu_tempuh3 = float(input("Masukkan waktu tempuh ketiga (T3): "))

# Menghitung jarak tempuh (S1, S2, S3)
jarak_tempuh1 = kecepatan1 * waktu_tempuh1
jarak_tempuh2 = kecepatan2 * waktu_tempuh2
jarak_tempuh3 = kecepatan3 * waktu_tempuh3

# Menghitung rata-rata jarak tempuh (Rata_jarak)
rata_jarak = (jarak_tempuh1 + jarak_tempuh2 + jarak_tempuh3) / 3

# Menampilkan hasil perhitungan
print(f"")
print(f"==================[Hasil Jarak Tempuh]==================")
print(f"Jarak Tempuh 1: {jarak_tempuh1}")
print(f"Jarak Tempuh 2: {jarak_tempuh2}")
print(f"Jarak Tempuh 3: {jarak_tempuh3}")
print(f"Rata-rata Jarak Tempuh: {rata_jarak}")

# -------------------------------------------------------------------------
