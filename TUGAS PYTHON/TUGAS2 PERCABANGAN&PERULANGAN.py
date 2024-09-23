anak = int(input('Masukkan jumlah anak kucing'))
for  i in range(anak, 0, -1):
    if i > 1:
        print('Anak kucing turun lah', i, 'Hilang satu tinggal', i - 1)
    elif i == 1:
        print('Anak kucing turunlah', i, 'Hilang semua tinggal induknya')