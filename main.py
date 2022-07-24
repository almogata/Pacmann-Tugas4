""" Library Management System

Modul ini adalah menu modul utama untuk Library Management System
Modul ini mengambil input berupa nomor menu dari user dan mengembalikan
modul lain sesuai dengan menu yang dipilih

"""

import pengembalian
import cari_buku
import tampilkan_peminjaman
import tampilkan_buku
import tampilkan_user
import peminjaman
import pendaftaran_buku
import pendaftaran_user
import koneksi

exit = False
while not exit:
 # Untuk looping ke main menu homepage sampai dengan menu exit(9) dipilih
  
    homepage = """
.................LIBRARY MANAGEMENT.................
----------------------------------------------------
    1. Pendaftaran User Baru
    2. Pendaftaran Buku Baru
    3. Peminjaman
    4. Tampilkan Daftar Buku
    5. Tampilkan Daftar User
    6. Tampilkan Daftar Peminjaman
    7. Cari Buku
    8. Pengembalian
    9. Exit
----------------------------------------------------
Masukkan Nomor Tugas:
====================================================
"""
    daftar_perintah = ("1","2","3","4","5","6","7","8","9")
    perintah = input(homepage)
    while perintah not in daftar_perintah:
     # Untuk looping ke main menu homepage jika menu yang 
     # diinput salah
      
        print("""
    
Masukkan angka 1 sampai 9""")
        perintah = input(homepage)
            
    if perintah == "9":
        exit = True
        print("Terima Kasih, Sampai Bertemu kembali")
        print("====================================================")
    elif perintah == "8":
        pengembalian.pengembalian_buku()
    elif perintah == "7":
        cari_buku.cari()
    elif perintah == "6":
        tampilkan_peminjaman.daftar_peminjaman()
    elif perintah == "5":
        tampilkan_user.list_user()
    elif perintah == "4":
        tampilkan_buku.list_buku()
    elif perintah == "3":
        peminjaman.pinjam()
    elif perintah == "2":
        pendaftaran_buku.daftar_buku()
    elif perintah == "1":
        pendaftaran_user.daftar_user()