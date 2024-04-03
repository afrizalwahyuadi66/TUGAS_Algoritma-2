# -------------------------------------------------------------------------
 # JUDUL  : PROGRAM ANGKA 0-9 KE BENTUK TEKS
 # INPUT  : Memasukan angka dari 0-9
 # PROSES : Menampilkan teks dari angka 0-9 tidak boleh lebih dan kurang
 # OUTPUT : Teks dari angka yang kita input jika lebih/kurang output akan 
		menampilkan teks "Salah entri: ketik bilangan 0..9"
# -------------------------------------------------------------------------

# ALGORITMA----------------------------------------------------------------

# Menerima input bilangan integer dari pengguna
X = int(input("Masukkan sebuah bilangan integer (0 s/d 9): "))

# Menampilkan tulisan teks bilangan
if 0 <= X <= 9:
    if X == 0:
        print("nol")
    elif X ==1:
        print("satu")
    elif X == 2:
        print("dua")
    elif X == 3:
        print("tiga")
    elif X == 4:
        print("empat")
    elif X == 5:
        print("lima")
    elif X == 6:
        print("enam")
    elif X == 7:
        print("tujuh")
    elif X == 8:
        print("delapan")
    elif X == 9:
         print("sembilan")
else:
    print("")
    print("---------------------------------")
    print("Salah entri: ketik bilangan 0..9")

# -------------------------------------------------------------------------
