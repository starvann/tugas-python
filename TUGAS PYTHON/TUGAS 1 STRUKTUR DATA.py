buku_telepon = {}

for i in range(1, 6):
    nama = input(f"Masukkan nama: ")
    no_hp = input(f"Masukkan nomor telepon: ")
    buku_telepon[nama] = no_hp

print("\nBuku Telepon")
for index, (nama, no_hp) in enumerate(buku_telepon.items(), 1):
    print(f"{index}. {nama} = {no_hp}")