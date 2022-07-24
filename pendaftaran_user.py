"""Modul Pendaftaran User

Modul ini digunakan untuk melakukan pendaftaran user baru
Menerima input dari user untuk dimasukkan ke database

"""

import koneksi
from mysql.connector import Error

def daftar_user():
    # Menerima input dari user
    nama_user = input("Masukkan Nama User: ")
    tanggal_lahir = input("Masukkan Tanggal Lahir (YYYY-MM-DD): ")
    pekerjaan = input("Masukkan Pekerjaan: ")
    alamat = input("Masukkan Alamat: ")
    data = (nama_user, tanggal_lahir, pekerjaan, alamat)
     # Values yang akan dimasukkan ke dalam query
     
    try:
        query = """
INSERT INTO daftar_user(U_Name,Tgl_Lahir,Pekerjaan,Alamat) VALUES(%s,%s,%s,%s)
"""
        mydb = koneksi.sambungkan()
        mycursor = mydb.cursor()
        mycursor.execute(query, data)
        mydb.commit()
        print('Query berhasil dieksekusi')
        print('..........................')
        print('Data berhasil ditambahkan!')
    except Error as err:
        print(f"Error: {err}")
    



