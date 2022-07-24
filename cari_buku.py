"""Modul Pencarian Buku

Modul ini digunakan untuk melakukan pencarian buku
Menerima input dari user berupa keyword untuk dicari di database

"""

import koneksi
import pandas as pd
from mysql.connector import Error

def cari():
    
    try:
        mydb = koneksi.sambungkan()
        mycursor = mydb.cursor()
        mycursor.execute("DESCRIBE daftar_buku")
        describe_buku = pd.DataFrame(mycursor.fetchall())
        nama_kolom = describe_buku.iloc[:, 0]
        # Mengambi judul kolom
    
        keyword = input("Masukkan Keyword Yang Ingin Dicari: ")
        mycursor.execute("SELECT * FROM daftar_buku WHERE MATCH(Nama_Buku, Kategori) \
                         AGAINST (%s IN NATURAL LANGUAGE MODE)",(keyword,))
        hasil = mycursor.fetchall()
        jumlah_hasil = len(hasil)
        if jumlah_hasil < 1:
         # Cek apakah keyword ditemukan atau tidak
            print("Buku Tidak Ditemukan")
        else:
            hasil = pd.DataFrame(hasil)
            hasil = hasil.rename(columns = nama_kolom)
            # Mengganti judul kolom dari index menjadi nama_kolom
            print(hasil)
    except Error as err:
        print(f"Error: {err}")