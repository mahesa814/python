#Tugas Mandiri 1 

# Seorang pedagang mangga menjual dagangannya
# yang setiap kg mangga dihargai dengan harga
# tertentu. Setiap pembeli membayar harga
# mangga yang dibeli nya berdasarkan berat.
# • Tentukan algoritma pedagang untuk menentukan
# harga yang harus dibayar pembeli.
# • Identifikasi masalah
# • Input: harga per kg(hrg), berat pembelian(brt)
# • Output: harga yang dibayar pembeli(byr)

from socketserver import ThreadingUnixDatagramServer


print("**** Tugas 1  *****".center(50))


harga_kg = int(input("Masukan harga Perkilogram = "))

berat_kg = int(input("masukan berapa kg yang dibeli = "))

hasil = harga_kg*berat_kg

print(hasil)

uang = int(input('masukan uang yang dibayar oleh pembeli ='))


bayar = hasil-uang
print("Jadi kembalian Nya" , bayar)

# Tugas Mandiri 2

# Ibu pergi ke pasar membeli telur sebanyak 5 kilogram
# untuk membuat kue, harga 1 kilo gram telor adalah 26000
# perkilogram. Untuk pergi ke pasar ibu harus naik angkot pp
# (pulang pergi) dengan tarip Rp 3500 sekali naik angkot.
# Pertanyaan: Berapakah sisa uang jika ibu membawa uang
# sebesar Rp 200.000,-
# Identifikasi masalah
# Input: berat telur(brt), harga telur (hrg), transport(ongkos)
# uang ibu(uang)
# Output: sisa uang(sisa)
# Buatlah Programnya dengan Python!
print("**** Tugas 2  *****".center(50))

brt_telur = int(input("masukan berat telur = "))

harga_telur = int(input("masukan harga telur yang harus dibayar = "))

transport = int(input("masukan harga transport = "))

hasil = (brt_telur*harga_telur)-transport

uang_sisa = 200000 - hasil  

print("jadi uang sisa ibu adalah = " ,uang_sisa)


