## REKURSIF

def fpb(a, b):
    if(b == 0):
        return a
    else:
        return fpb(b, a % b)
    
a = int(input('Masukkan angka pertama: '))
b = int(input('Masukkan angka kedua: '))
hitung_FPB = fpb(a, b)
print('FPB adalah',hitung_FPB)