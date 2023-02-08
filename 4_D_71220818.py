
def hitungnilai() :
    nilaiharian=0
    nilaiuts=0
    nilaiuas=0
    x=1
    for nilaimasuk in range(2):
        print("--------Nilai ke",x,"--------")
        x+=1
        harian=int(input("Nilai Harian :"))
        uts=int(input("Nilai UTS :"))
        uas=int(input("Nilai UAS :"))
        nilaiharian += harian
        nilaiuts += uts
        nilaiuas += uas

    totalnilai=(((nilaiharian*(30/100))+(nilaiuts*(30/100))+(nilaiuas*(40/100)))/2)
    

    print("Total nilai yang didapat :",totalnilai)
    if totalnilai >= 80:
        print("Total Nilai dalam Huruf : A")
    elif totalnilai>59 and totalnilai<80:
        print("Total Nilai dalam Huruf : B")
    elif totalnilai>39 and totalnilai<60:
        print("Total Nilai dalam Huruf : C")
    elif totalnilai>19 and totalnilai<40:
        print("Total Nilai dalam Huruf : D")
    elif totalnilai<20:
        print("Total Nilai dalam Huruf : E")


hitungnilai()
