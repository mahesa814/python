from unicodedata import name


tarif = 100
langganan = 3000 * 30
jml_pulsa = 235

tagihan_langganan = langganan+(jml_pulsa*tarif)
print("Tagihan Langganan",tagihan_langganan)

jam = 144/2
menit = 14400/120
milisecond = 144000/(3600*2)
print(jam)
print(menit)
print(milisecond)

lama_perjam = 100/80
print("Menempuh Berapa lama : ",lama_perjam,'Jam')

harga_satu = 72
tiga_lusin = 36
jual = 500

hasil = tiga_lusin*jual
print(hasil)

print("*****")

hasil2 = 300/25
print(hasil2)

semangka = 1500
melon = 3000
labu = 6000
uang_adi = 50000
jumlah_semangka= int(input("Masukan Jumlah Semangka Yang Mau Dibeli : "))
jumlah_melon= int(input("Masukan Jumlah Melon Yang Mau Dibeli : "))
jumlah_labu= int(input("Masukan Jumlah Labu Yang Mau Dibeli : "))
beli_semangka = semangka*jumlah_semangka
beli_melon = melon*jumlah_melon      
beli_labu = labu*jumlah_labu

print("Harga Semangka Total nya : ", beli_semangka)
print("Harga Melon Total nya : ", beli_melon)
print("Harga Labu Total nya : ", beli_labu)

print("**** Total Jumlah Yang Dibeli Masing Masing Buah ***".center(30))
print("Beli Jumlah semangka : ",jumlah_semangka)
print("Beli Jumlah Melon : ",jumlah_melon)
print("Beli jumlah Labu : ",jumlah_labu)
print("Jadi Jumlah Harga Yang di beli : ", beli_labu + beli_semangka + beli_melon)


print("soal selanjutnya")

