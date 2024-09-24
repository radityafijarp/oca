print("Barang apa yang akan Anda beli? (ketik 1 untuk barang baru, ketik 2 untuk barang lama")
jenis_barang=input("Masukan pilihan Anda: ")
harga_barang=int(input("Masukan Harga Barang: "))

if jenis_barang=="1":
    diskon=0.1
    harga_diskon=harga_barang-(harga_barang*diskon)
    print("harga yang harus dibayarkan (dalam rupiah): ",harga_diskon)
elif jenis_barang=="2":
    if harga_barang>200000:
        diskon=0.25
    elif harga_barang>50000:
        diskon=0.2
    else:
        diskon=0.15
        
    harga_diskon=harga_barang-(harga_barang*diskon)
    print("harga yang harus dibayarkan (dalam rupiah): ",harga_diskon)
else:
    print("Tidak ada pilihan ",jenis_barang)