pembeli = input('masukan nama pembeli : ')
no_hp = int(input('masukan no phone : '))
jurusan = input('Masukan Jurusan SBL/YG/JG ; ')

if jurusan == 'SBL':
    nama_jurusan = 'Surabaya'
    harga = 50000
elif jurusan == 'YG':
    nama_jurusan = 'Yogyakarta'
    harga = 100000
else:
    nama_jurusan = 'Jungle'
    harga = 200000

jumlah = int(input('masukan jumlah beli : '))

if jumlah >= 3:
    potongan = (jumlah*harga)*0.1
else:
    potongan = 0

total = (jumlah*harga)-potongan
print("----- Penjualan Tiket Bos XYZ ------")
print("Nama Pembeli : ", pembeli)
print("No Ponsel : ", no_hp)
print("Kode Jurusan Yang dipilih : ", jurusan)
print('Harga : ', harga)
print('jumlah yang dibeli', jumlah)
print('------------')

print('potongan yang didapat : ', potongan)
print('total bayar : ', total)
ubay = int(input('Masukan Uang Yang di Bayar : '))
uangkembali = ubay - total
print("uang Kembali :", uangkembali)
