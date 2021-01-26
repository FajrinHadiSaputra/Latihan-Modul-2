print('Selamat Datang Di toko buah')
print('1. Apel    : Rp. 25.000 \n2. Mangga  : Rp. 15.000 \n3. Kiwi    : Rp. 20.000 \n4. Alpukat : Rp. 30.000')
buah=input('Masukan Buah Yg Ingin Dibeli : ')
uang=float(input('Masukan uang anda : '))
jumlah_beli=int(input('Masukan jumlah buah yang anda beli: '))

if (buah=='1'):
    buah_dibeli=25000
    fruit='Apel'

elif (buah=='2'):
    buah_dibeli=15000
    fruit='Mangga'

elif (buah=='3'):
    buah_dibeli=20000
    fruit='kiwi'

elif (buah=='4'):
    buah_dibeli=30000
    fruit='Alpukat'

total_dibeli=(jumlah_beli*buah_dibeli)

if (jumlah_beli > 5):
    diskon=(total_dibeli*5/100)

elif (jumlah_beli < 5):
    diskon=(0)

total_harga=(total_dibeli-diskon)
kembalian=(uang-total_harga)
print('Total bayar         :  Rp.',total_harga)
print('Uang kembalian anda :  Rp.',kembalian)
print('Buah yang anda beli : ',fruit)
print('Jumlah buah dibeli  : ',jumlah_beli,'Kg')