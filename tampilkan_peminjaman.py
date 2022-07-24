"""Modul Menampilkan Daftar Peminjaman

Modul ini digunakan untuk manmpilkan daftar peminjaman

"""

import koneksi
import pandas as pd
from mysql.connector import Error



def daftar_peminjaman():
    print('..............................Daftar Peminjaman......................................')
    print('-------------------------------------------------------------------------------------')
    mydb = koneksi.sambungkan()
    query = 'SELECT * FROM peminjaman'
    query_describe = 'DESCRIBE peminjaman'
    mycursor = mydb.cursor()
    result = None
    nama_kolom = None

    try:
        mycursor.execute(query_describe)
        describe_user = pd.DataFrame(mycursor.fetchall())
        nama_kolom = describe_user.iloc[:, 0]
         # Untuk mengambil judul kolom
    except Error as err:
        print(f"Error: {err}")
    
    try:
        mycursor.execute(query)
        result = pd.DataFrame(mycursor.fetchall())
        result = result.rename(columns = nama_kolom)
         # Mengganti judul kolom dari index menjadi nama_kolom
        print(result)
        print('-------------------------------------------------------------------------------------')
        return pd.DataFrame(result)
    except Error as err:
        print(f"Error: {err}")
