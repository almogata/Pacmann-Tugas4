"""Modul Pengembalian Buku

Modul ini digunakan untuk melakukan pengembalian buku
Menerima input dari user untuk dimasukkan ke database

"""

import koneksi
import pandas as pd
from mysql.connector import Error
from datetime import date

def pengembalian_buku():
    
    today = date.today()
    mydb = koneksi.sambungkan()
    mycursor = mydb.cursor()
    
    try:
        mycursor.execute("SELECT Id_User FROM peminjaman WHERE Tanggal_Kembali IS NULL")
        list_peminjaman = mycursor.fetchall()
         # Mengambil daftar peminjaman yang tanggal kembali masih kosong
        if len(list_peminjaman) > 0:
         # jika list peminjaman tidak kosong, lanjutkan   
            id_peminjam = []
            for x in list_peminjaman:
             # Convert id peminjam menjadi string untuk dibandingkan dengan input user
                id_peminjam.append(str(x[0]))
            cek_id_peminjam = input("Masukkan ID Peminjam: ")
            while cek_id_peminjam not in id_peminjam:
             # Looping jika id peminjam yang diinput user tidak ditemukan
                print("ID Peminjam Tidak Ditemukan, Silahkan Masukkan ID Yang Sesuai")
                cek_id_peminjam = input("Masukkan ID Peminjam: ")
            print("ID Peminjam: "+cek_id_peminjam)
            
            mycursor.execute("SELECT Id_Buku, Nama_Buku FROM peminjaman WHERE Id_User = %s \
                              AND Tanggal_Kembali IS NULL", (cek_id_peminjam,))
            list_pinjam_buku = mycursor.fetchall()
             # Menampilkan daftar buku yang dipinjam dan belum dikembalikan
            id_buku = []
            print("Buku Yang Dipinjam:")
            result = pd.DataFrame(list_pinjam_buku)
            print(result)
            
            for y in list_pinjam_buku:
             # Convert id buku menjadi string untuk dibandingkan dengan input user
                id_buku.append(str(y[0]))
            cek_id_buku = input("Masukkan ID Buku Yang Akan Dikembalikan: ")
            while cek_id_buku not in id_buku:
             # Looping jika id buku yang diinput user tidak ditemukan
                print("ID Buku Tidak Ditemukan, Silahkan Masukkan ID Yang Sesuai")
                cek_id_buku = input("Masukkan ID Buku Yang Akan Dikembalikan: ")
            mycursor.execute("UPDATE peminjaman SET Tanggal_Kembali = %s WHERE Id_User = %s \
                              AND Id_Buku = %s",(today, cek_id_peminjam, cek_id_buku))
            mycursor.execute("UPDATE daftar_buku SET Stock = Stock+1 WHERE Id_Buku = %s",(cek_id_buku,))
             # Memasukkan data pengembalian ke database
            mydb.commit()
            print("Buku telah berhasil dikembalikan, terima kasih")
            print("============================================================")
            
        else:
         # Jika tidak ada buku yang sedang dipinjam dan belum dikembalikan
            print("Tidak Ada Buku Yang Dipinjam")
            
    except Error as err:
        print(f"Error: {err}")
  