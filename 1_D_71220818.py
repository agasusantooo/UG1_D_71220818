totalbelanja = 0

print("=========== KASIR ============")

for hitungtotal in range(1) :
    hargabarang = int(input("Harga Barang :"))
    totalbelanja = totalbelanja + hargabarang
    tambahbarang = input("Apakah anda membeli barang lagi? [yes/no] :")
    while (tambahbarang == "yes") :
        for hitungtotal in range(1) :
            hargabarang = int(input("Harga Barang :"))
            totalbelanja = totalbelanja + hargabarang
            tambahbarang = input("Apakah anda membeli barang lagi? [yes/no] :")
    if(tambahbarang == "no") :
        print("TOTAL BELANJA :", totalbelanja)
    else :
        print("INVALID")