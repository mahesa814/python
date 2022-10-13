nim = int(input("Masukan Nomor Nim Anda          : "))
nama = str(input("Masukan Nama Anda              : "))
jurusan = str(input("Masukan Kode Jurusan SI/SIA :"))
print("Nis          : ", nim)
print('Nama         :', nama)
print('Kode Jurusan : ',jurusan)
if jurusan == "SI" :
    nama_jurusan = "Sistem Informasi"
    print("Nama Jurusan : ",nama_jurusan)
    biaya_kuliah = 2400000
    print("Biaya Kuliah : ",biaya_kuliah)
    
elif jurusan == "SIA" :    
    nama_jurusan = "Sistem Informasi Akuntasnai"
    print("Nama Jurusan : ",nama_jurusan)
    biaya_kuliah = 2000000
    print("Biaya Kuliah : ",biaya_kuliah)
else :
    print("Maaf Kode Jurusan Kamu Tidak Terdaftar")
