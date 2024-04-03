# -------------------------------------------------------------------------
 # JUDUL  : PROGRAM NILAI RAPORT
 # INPUT  : Angka Nilai dari Semua Hasil UTS, UAS, TUGAS, KEHADIRAN
 # PROSES : Mengihtung Seluruh Nilai dan Menentukan Indeks Mutu
 # OUTPUT : Nilai Akhir dan Indeks Mutu
# -------------------------------------------------------------------------

# ALGORITMA----------------------------------------------------------------

# Input nilai UTS, UAS, TUGAS, dan KEHADIRAN
UTS = float(input("Masukkan nilai UTS (0-100): "))
UAS = float(input("Masukkan nilai UAS (0-100): "))
TUGAS = float(input("Masukkan nilai TUGAS (0-100): "))
KEHADIRAN = float(input("Masukkan nilai KEHADIRAN (0-16): "))

# Hitung KEHADIRAN
KEHADIRAN = (KEHADIRAN / 16) * 100

# Hitung Nilai Akhir (NA)
NA = (0.3 * UTS) + (0.4 * UAS) + (0.2 * TUGAS) + (0.1 * KEHADIRAN)

# Tentukan Indeks Mutu (IM) berdasarkan Nilai Akhir (NA)
if 0 <= NA <= 100:
    if NA > 80:
        IM = 'nilai A'
    elif NA > 65:
        IM = 'nilai B'
    elif NA > 50:
        IM = 'nilai C'
    elif NA > 40:
        IM = 'nilai D'
    else:
        IM = 'nilai E'
else:
    IM = 'Salah nilai'

# Tampilkan Nilai Akhir dan Indeks Mutu
print("===========================")
print(f"Nilai Akhir (NA)    : {NA:.2f}")
print(f"Indeks Mutu (IM)    : {IM}")
print("===========================")

# -------------------------------------------------------------------------
