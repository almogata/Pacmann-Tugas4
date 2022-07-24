""" Modul Koneksi

Modul ini digunakan untuk membuat koneksi ke database mysql

"""

import mysql.connector 
from mysql.connector import Error

def sambungkan():
# membuat koneksi ke database
    nama_host = "localhost" # disesuaikan dengan nama komputer yang digunakan
    user = "pacmann" # disesuaikan dengan nama user yang digunakan untuk terkoneksi ke server
    password = "" # disesuaikan dengan password yang dibuat
    db = "lib_man_sys" # disesuaikan dengan nama database yang akan digunakan    
    mydb = None
    try:
        mydb = mysql.connector.connect(
            host = nama_host,
            user = user,
            passwd = password,
            database = db
        )
    except Error as err:
        print(f"Error: {err}")
    return mydb
    
 
 
