harga = float(input('Masukkan tarif tiket kereta Rp.'))
umur = int(input('Masukkan usia penumpang '))

if 0 <= umur <=4:
    hasil1 = (harga*100)/100
    hasil1 = 0
    print('Harga tiket setelah diskon Rp.', hasil1)
elif 5 <= umur <=12:
    hasil2 = (harga*50)/100
    print('Harga tiket setelah diskon Rp.', hasil2)
else:
    print('Tidak mendapatkan diskon, total harga masih sama sebesar Rp.', harga )