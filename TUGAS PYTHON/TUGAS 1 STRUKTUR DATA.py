phonelist = []
for i in range(1,6):
    nama = input('Masukkan nama pemilik nomor')
    nomor = input ('Masukkan nomor')

    print('\n Phone book')
    print(nama, '=', nomor)

print('\nPhone Book'.center(50))
for index, (nama,nomor) in enumerate(phonelist.items(),1):
    print(f'{index}. {nama} = {nomor}')