# Kelom 2
nama_diagnosa = input('masukan gejala penyakit = ');

demam = 'dehidrasi';

covid = 'lidah tidak berasa'

lambung = 'perut sakit';

sariawan = 'gusi perih';

galau = 'kamu tidak memiliki pasangan'

penyakit = "Penyakit Kamu Adalah :"
gejala = "Mungkin Kamu Mengalamai Gejala  :"
# demam = "nyeri"
if nama_diagnosa == demam : 
    print(penyakit , "Demam")
elif nama_diagnosa == sariawan :
    print(penyakit , "Sariawan")
elif nama_diagnosa == covid :
    print(gejala, "Covid")
elif nama_diagnosa == lambung :
    print(gejala, "Lambung")
elif nama_diagnosa == galau : 
    print('Makanya Good Money Biar Bisa Cewe Pada Nyamperin')
else :
    print("Penyakit kamu tidak terdaftar di list yang kami tahu")