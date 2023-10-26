angka_pertama = 12
angka_kedua = 5
sisa = 0
hasil_pembagian = 0

if(angka_kedua > angka_pertama):
    print("Angka kedua lebih besar daripada angka pertama")
else:
    while angka_pertama > 0:
        angka_pertama = angka_pertama - angka_kedua

        if angka_pertama <= 0:
            if(angka_pertama == 0):
                sisa = 0
            else:
                sisa = angka_kedua + angka_pertama
            break
        else:
            hasil_pembagian += 1


    if(sisa > 0):
        mix = str(hasil_pembagian) + "." + str(sisa)
        print("Total Pembagian:", mix)
    else:
        print("Hasil Pembagian:", hasil_pembagian)