def kasir():
    total_harga = 0
    belanjaan = []

    print("Selamat datang di TOKO SEMOGA LANCAR")
    while True:
        nama_barang = input("Masukkan nama barang (atau ketik 'selesai' untuk mengakhiri): ")
        if nama_barang.lower() == 'selesai':
            break
        
        try:
            jumlah = int(input(f"Masukkan jumlah {nama_barang}: "))
            harga = float(input(f"Masukkan harga satuan {nama_barang}: "))
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka yang benar.")
            continue
        
        total_per_barang = jumlah * harga
        total_harga += total_per_barang
        
        belanjaan.append({
            'nama': nama_barang,
            'jumlah': jumlah,
            'harga': harga,
            'total': total_per_barang
        })
    
    print(f"\nTotal harga seluruh belanja: Rp {total_harga:.2f}")
    
    with open('invoice.txt', 'w') as file:
        file.write("Rincian Belanja\n")
        file.write("===============================\n")
        for item in belanjaan:
            file.write(f"{item['nama']} x {item['jumlah']} @ Rp {item['harga']:.2f} = Rp {item['total']:.2f}\n")
        file.write("===============================\n")
        file.write(f"Total Belanja: Rp {total_harga:.2f}\n")
    
    print("Invoice telah dibuat dengan nama 'invoice.txt'.")

kasir()