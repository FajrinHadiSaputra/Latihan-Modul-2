print('Selamat Datang Di toko buah')
print('1. Apel    : Rp. 25.000 \n2. Mangga  : Rp. 15.000 \n3. Kiwi    : Rp. 20.000 \n4. Alpukat : Rp. 30.000')
buah=input('Masukan Buah Yg Ingin Dibeli : ')
uang=float(input('Masukan uang anda : '))

if (buah=='1'):
    uang_pembeli=(uang-25000)
    fruit='Apel'

elif (buah=='2'):
    uang_pembeli=(uang-15000)
    fruit='Mangga'

elif (buah=='3'):
    uang_pembeli=(uang-20000)
    fruit='kiwi'

elif (buah=='4'):
    uang_pembeli=(uang-30000)
    fruit='Alpukat'

print('Uang kembalian anda : ',uang_pembeli)
print(fruit)