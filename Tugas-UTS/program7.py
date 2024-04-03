# -------------------------------------------------------------------------
 # JUDUL  : PROGRAM BUKTI TRANSAKSI
 # INPUT  : Angka "Masukkan sebuah bilangan integer (X): "
 # PROSES : Membuat Bukti Transaksi
 # OUTPUT : Struk Pembayaran
# -------------------------------------------------------------------------

import datetime

# ALGORITMA----------------------------------------------------------------

# Mendapatkan tanggal dan waktu saat ini
tanggal_waktu_sekarang = datetime.datetime.now()
hari = tanggal_waktu_sekarang.strftime("%A")
tanggal = tanggal_waktu_sekarang.strftime("%x")
waktu = tanggal_waktu_sekarang.strftime("%X")

# Menerima input jumlah pembelian dalam Rp.
jumlah_pembelian = float(input("Masukkan jumlah pembelian dalam Rp.: "))

# Menerima input jenis konsumen (1 untuk pelanggan, 2 untuk non-pelanggan)
jenis_konsumen = int(input("Masukkan jenis konsumen (1. Pelanggan; 2. Non-pelanggan): "))

# Inisialisasi potongan dan cashback
potongan = 0
cashback = 0

# Menghitung potongan untuk pelanggan
if jenis_konsumen == 1:
    potongan = 0.10 * jumlah_pembelian

# Menghitung cashback
cashback = int(jumlah_pembelian / 1000000) * 30000

# Menghitung total pembayaran setelah potongan dan cashback
total_pembayaran = jumlah_pembelian - potongan + cashback

# Menampilkan hasil transaksi
print(f"\n===== Struk Pembayaran =====")
print(f"Hari               : {hari}")
print(f"Tanggal            : {tanggal}")
print(f"Waktu              : {waktu}")
print(f"Jumlah Pembelian   : Rp. {jumlah_pembelian:,.2f}")
print(f"Potongan           : Rp. {potongan:,.2f}")
print(f"Cashback           : Rp. {cashback:,.2f}")
print(f"Total Pembayaran   : Rp. {total_pembayaran:,.2f}")
print("============================")

# -------------------------------------------------------------------------
