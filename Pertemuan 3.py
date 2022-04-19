#cara pertama
def bagi(x, y):
    bagi = x / y
    return bagi
    
def kali(x, y):
    kali = x * y
    return kali
#cara pertama


# cara kedua
def sisaBagi(x, y):
    return x % y

if __name__ == '__main__':
    x = int(input(' Masukkan nilai X = '))
    y = int(input(' Masukkan nilai Y = '))
    print()
    print(' Hasil pembagian = ',bagi(x, y))
    print(' Hasil perkalian = ',kali(x, y))
    print(' Hasil sisa bagi = ',sisaBagi(x, y))
quit()