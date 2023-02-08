jumlahkata=0
kalimat=input("Kalimat yang ingin diteliti :")
kalimat=kalimat.lower()
katayangdicari=input("Kata yang dicari:")
katayangdicari=katayangdicari.lower()
kalimat_list=kalimat.split()

for kata in kalimat_list:
    if katayangdicari == kata:
        jumlahkata += 1
        
print(jumlahkata)
