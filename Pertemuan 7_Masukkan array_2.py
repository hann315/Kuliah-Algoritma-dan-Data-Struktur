from array import *

arr = array('i',[])

def isiArray(x):
    j = 1
    while j <= x:
        baca = int(input('Angka ke['+str(j)+'] = '))
        arr.insert(j,baca)
        j += 1
        print()
        print('Hasil masukan angka')
        print(arr,'', end='')
              
if __name__ == '__main__':
    x = int(input("Masukkan banyaknya angka: "))
    isiArray(x)
    print()
quit()