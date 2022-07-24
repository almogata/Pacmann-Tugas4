"""Modul Pendaftaran Buku

Modul ini digunakan untuk melakukan pendaftaran buku baru
Menerima input dari user untuk dimasukkan ke database

"""

import koneksi
from mysql.connector import Error

def daftar_buku():
    mydb = koneksi.sambungkan()
    mycursor = mydb.cursor()
    # Menerima input dari user
    try:
        mycursor.execute("SELECT Id_Buku FROM daftar_buku")
        list_id_buku = mycursor.fetchall()
         # Mengambil list id buku yang sudah terdaftar
        
        id_buku = []
        for x in list_id_buku:
         # Convert id buku menjadi string untuk dicocokkan dengan input user
            id_buku.append(str(x[0]))
            
        cek_id_buku = input("Masukkan ID Buku: ")
        
        while cek_id_buku in id_buku:
         # Looping jika user memasukkan id buku yang sudah terdaftar
            print("ID Sudah Ada, Silahkan Masukkan ID Yang Lain")
            cek_id_buku = input("Masukkan ID Buku: ")
            
        nama_buku = input("Masukkan Nama Buku: ")
        kategori = input("Masukkan Kategori Buku: ")
        stock = input("Masukkan Stock Buku: ")
        data = (cek_id_buku, nama_buku, kategori, stock)
        
        query = """
INSERT INTO daftar_buku(Id_Buku,Nama_Buku,Kategori,Stock) VALUES(%s,%s,%s,%s)
"""
        mycursor.execute(query, data)
         # Memasukkan data input user ke dalam database
        mydb.commit()
        print('Query berhasil dieksekusi')
        print('..........................')
        print('Data berhasil ditambahkan!')
        
    except Error as err:
        print(f"Error: {err}")
       
   

