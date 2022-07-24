# Pacmann-Tugas4
Pacmann Kelas Python - Tugas 4

Tujuan pengerjaan project ini adalah membuat sebuah Library Manaement System (LMS) sederhana.
Project ini dibuat dalam rangka memenuhi Tugas dari kelas Python Pacmann.

Detail/deskripsi file tugas:
1. LMS.sql: query SQL untuk membuat database lib_man_sys. Database terdiri dari 3 table yaitu daftar_user, daftar_buku, peminjaman.
2. main.py: modul utama LMS, mengambil input dari user untuk diterjemahkan menjadi subtugas yang dijalankan oleh submodul
3. pendaftaran_user.py: modul pendaftaran user, mengambil input data user untuk dimasukkan ke database
4. pendaftaran_buku.py: modul pendaftaran buku, mengambil input data buku untuk dimasukkan ke database
5. tampilkan_user.py: modul untuk menampilkan seluruh user terdaftar
6. tampilkan_buku.py: modul untuk menampilkan seluruh buku terdaftar
7. peminjaman.py: modul untuk melakukan peminjaman, mengambil input id_user dan id_buku untuk dimasukkan ke database
8. pengembalian.py: modul untuk melakukan pengembalian, mengambil input id_user dan id_buku untuk dimasukkan ke database
9. tampilkan_peminjaman.py: modul untuk menampilkan seluruh peminjaman yang sudah dilakukan
10. cari_buku.py: modul untuk melakukan pencarian buku, mengambil input keyword dari user untuk dicari di kolom kategori dan nama_buku dari tabel daftar_buku
11. Test_Case.docx: hasil pengetesan program

Cara penggunaan program:
1. Jalankan query LMS.sql di mysql workbench, sesuaikan host, username, dan password
2. Copykan seluruh file ke folder lokal
3. Jalankan shell di folder tersebut
4. masukkan command python/python3 main.py
5. Ikuti petunjuk sesuai program

Hasil test case:
Hasil test case (terlampir) menunjukkan program telah berhasil memenuhi requirements yang dibutuhkan

Saran perbaikan:
1. Perlu tambahan fitur untuk mengecek dan membatasi input dari user
2. Perlu ditambahkan fitur untuk menghapus user dan buku
