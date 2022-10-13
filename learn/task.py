# 1 . agung baitul himah mempunyai gaji pokok kemudian mendapat tunjangan sebesar 5% dari gaji pokok dan mempunya hutang potongan sebesar #2 juta berapa gaji bersih agung baitul hikmah dalam 1 bulan 
# lembur 10000 per jam dalam satu minggu agung lembur 5 jam,
# mendapat  tunjangan bensin 20 liter dengan harga perliternya 10.000
# berapa gaji bersih yang di terima dalam 1 bulan
from cgi import print_arguments


gaji = int( input ( " Silahkan Gaji = "))
tunjangan =  gaji*5/100
potongan_gaji = 2000000
hasil_1 = (gaji+tunjangan) - potongan_gaji
lembur = 10000  * 20
tunjangan_bensin = 10000 * 20
hasil = hasil_1 + lembur + tunjangan_bensin
print(hasil_1)
print(hasil)
# print(tunjangan)
# print('Jadi Gaji Agung' , hasil) 




