"""Modul Menampilkan User

Modul ini digunakan untuk manmpilkan daftar user

"""

import koneksi
import pandas as pd
from mysql.connector import Error


def list_user():
    print('......................Daftar User..............................')
    print('---------------------------------------------------------------')
    mydb = koneksi.sambungkan()
    query = 'SELECT * FROM daftar_user'
    query_describe = 'DESCRIBE daftar_user'
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
        print('---------------------------------------------------------------')
        return pd.DataFrame(result)
    except Error as err:
        print(f"Error: {err}")
    
    
