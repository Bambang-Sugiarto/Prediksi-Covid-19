#Jumlah Rata-Rata Orang Bertemu Pasien Covid-19
R = int(input('Masukan Jumlah Rata-Rata Orang Bertemu Pasien Covid-19 : '))
#Peluang Tertular
P = float(input('Masukan Peluang Tertular (ex 0.1, 0.01, 0.5 dst) : '))
#Jumlah Kasus Perhari
Nh = int(input('Masukan Jumlah Kasus Perhari : '))
#Hari ke x
x = int(input('Hari ke : '))
#rumus menggunakan persamaan eksponen
pangkat = (1 + R * P)**x
Nx = int(pangkat*Nh)
print('')
print('Hari ke -',x)
print('Jumlah Kasus Perhari :',Nh)
print('Peluang Tertular : ',P)
print('Jumlah Rata-Rata Orang Bertemu Pasien Covid-19 : ',R)
print('--------------------------------------------------------')
print('HASIL -> Jumlah Pasien Di Hari Ke - ',x,' : ',Nx, 'orang')
print('--------------------------------------------------------')
