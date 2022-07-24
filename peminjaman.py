"""Modul Peminjaman Buku

Modul ini digunakan untuk melakukan peminjaman buku
Menerima input dari user untuk dimasukkan ke database

"""

import koneksi
import pandas as pd
from mysql.connector import Error
from datetime import date


def pinjam():

    today = date.today()
    mydb = koneksi.sambungkan()
    mycursor = mydb.cursor()
    
    try:
        mycursor.execute("SELECT Id_User FROM daftar_user")
        list_user = mycursor.fetchall()
         # Mengambil list user yang sudah terdaftar
        
        id_user = []
        for x in list_user:
         # Convert id user menjadi string untuk dicocokkan dengan input user
            id_user.append(str(x[0]))
            
        cek_id_peminjam = input("Masukkan ID Peminjam: ")
        
        while cek_id_peminjam not in id_user:
         # Looping jika user memasukkan id user yang belum terdaftar
            print("ID User Tidak Ditemukan, Silahkan Masukkan ID Yang Sesuai")
            cek_id_peminjam = input("Masukkan ID Peminjam: ")
            
        print("ID User: "+cek_id_peminjam)
        
    except Error as err:
        print(f"Error: {err}")
        
    try:
        mycursor.execute("SELECT U_Name FROM daftar_user WHERE Id_User = %s", (cek_id_peminjam,))
        nama_user = mycursor.fetchall()[0][0]
         # Mengambil nama user
        print("Nama User: "+nama_user)
    except Error as err:
        print(f"Error: {err}")
        
    try:
        mycursor.execute("SELECT Id_Buku FROM daftar_buku")
        list_buku = mycursor.fetchall()
         # Mengambil list user yang sudah terdaftar
        
        id_buku = []
        for x in list_buku:
         # Convert id user menjadi string untuk dicocokkan dengan input user
            id_buku.append(str(x[0]))
        cek_id_buku = input("Masukkan ID Buku: ")
        
        while cek_id_buku not in id_buku:
         # Looping jika user memasukkan id yang belum terdaftar
            print("ID Buku Tidak Ditemukan, Silahkan Masukkan ID Yang Sesuai")
            cek_id_buku = input("Masukkan ID Buku: ")  
        print("ID Buku: "+cek_id_buku)
        
    except Error as err:
        print(f"Error: {err}")
        
    try:
        mycursor.execute("SELECT Nama_Buku FROM daftar_buku WHERE Id_Buku = %s", (cek_id_buku,))
        nama_buku = mycursor.fetchall()[0][0]
         # Mengambil nama buku
        print("Judul Buku: "+nama_buku)
    except Error as err:
        print(f"Error: {err}")
        
    try:
        mycursor.execute("SELECT Stock FROM daftar_buku WHERE Id_Buku = %s", (cek_id_buku,))
        stock_buku = mycursor.fetchall()
        sisa_stock_buku = stock_buku[0][0]
         # Mengambil stock buku awal
        print("Stock Buku: "+str(sisa_stock_buku))
        
        if sisa_stock_buku < 1:
            print("Buku Tidak Tersedia")
        else:
            print("Buku Dipinjamkan ke: "+ nama_user)
            sisa_stock_buku -= 1
            print("Sisa Stock Buku: "+str(sisa_stock_buku))
            mycursor.execute("UPDATE daftar_buku SET Stock = %s WHERE Id_Buku = %s" %(sisa_stock_buku,cek_id_buku))
            mycursor.execute("INSERT INTO peminjaman(Id_User, Nama_User, Id_Buku, Nama_Buku, Tanggal_Pinjam)\
                                     VALUES(%s,%s,%s,%s,%s)",(cek_id_peminjam, nama_user, cek_id_buku, nama_buku, today))           
            mydb.commit()
             # Memasukkan data peminjaman ke database
             
    except Error as err:
        print(f"Error: {err}")
    
    