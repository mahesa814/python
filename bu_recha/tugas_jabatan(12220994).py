print("**** Harus Pake Huruf Kapital Saat Pemilihan Pendidikan")
nama = str(input('Masukan Nama :'))
gaji_pokok = int(input('Masukan Gaji Pokok :'))
print('====== Tugas Jabatan  =======')
print('Golongan       Persentase ')
print('   1               5%')
print('   2               10%')
print('   3               15%')

pilih_golongan = int(input("Masukan Golongan :"))

print('====== Tugas Pendidikan  =======')
print('Pendidikan       Persentase ')
print('   SMA               2.5%')
print('   D1                5%')
print('   D3                20%')
print('   S1                30%')

pilih_pendidikan = str(input("Masukan Pendidikan :"))

lembur = int(input('Masukan Jam Lembur :'))

if pilih_golongan == 1:
    pg = gaji_pokok * 0.05
    golongan = 1
elif pilih_golongan == 2:
    pg = gaji_pokok * 0.1
    golongan = 2
elif pilih_golongan == 3:
    pg = gaji_pokok * 0.15
    golongan = 1
else:
    print('Maaf Golongan Kamu Tidak terdaftar')

if pilih_pendidikan == "SMA":
    pp = gaji_pokok * 0.025
    pendidikan = "SMA"
elif pilih_pendidikan == "D1":
    pp = gaji_pokok * 0.5
    pendidikan = "D1"
elif pilih_pendidikan == "D3":
    pp = gaji_pokok * 0.2
    pendidikan = "D3"
elif pilih_pendidikan == "S1":
    pp = gaji_pokok * 0.3
    pendidikan = "S1"
else:
    print('Maaf Tunjangan Kamu Tidak terdaftar')

print("======== Details Kariyawan ==========")

print("Nama                 : ", nama)
print("Gaji Pokok           : ", gaji_pokok)
print("Golongan Kamu Kamu   : ", pendidikan)
if lembur > 8:
    jam_lembur = lembur-8
    print("Jam Lembur Kamu      : ", jam_lembur)
    lembur_jam = jam_lembur*26*3500
    print("Jadi Kamu Selama Sebulan Sudah Lembur : ", lembur_jam, "Jam")
else:
    lembur_jam = 0
    print("Jam Lembur           : ", lembur_jam)

total = gaji_pokok+pg+pp+lembur_jam
print("Jadi Total Gaji Bersih kami adalah : Rp.", total)
