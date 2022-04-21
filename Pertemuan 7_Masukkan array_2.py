from array import *

arr = array('i',[])

def isiArray(x):
    j = 1
    while j <= x:
        arr.append(int(input("Masukkan angka baru: ")))
        j += 1
        print()
        print('Hasil masukkan angka: ')
        print(arr,'', end='')
              
if __name__ == '__main__':
    x = int(input("Masukkan banyaknya angka: "))
    isiArray(x)
    print()
quit()