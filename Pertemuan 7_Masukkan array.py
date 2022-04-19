from array import *

arr = array('i',[10,20,30,40,50])

if __name__ == '__main__':
    arr.insert(4,65)
    arr.append(int(input("Tambah angka baru: ")))
    for i in arr:
        print(i)
        
quit()