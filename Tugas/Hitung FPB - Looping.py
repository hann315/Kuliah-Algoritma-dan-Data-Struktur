## LOOPING

def fpb(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            fpb = i
    return fpb
    
angka_Pertama = int(input('Masukkan angka pertama: '))
angka_Kedua = int(input('Masukkan angka kedua: '))
hitung = fpb(angka_Pertama, angka_Kedua)

print('FPB dari', angka_Pertama,'dan', angka_Kedua,'adalah',hitung)