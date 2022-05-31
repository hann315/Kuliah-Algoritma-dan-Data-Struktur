class Node:
    
    def __init__(isi, data):
                 isi.kiri = None
                 isi.kanan = None
                 isi.data = data
                 
    def TampilkanPohon(isi):
                 if isi.kiri:
                     isi.kiri.TampilkanPohon()
                 print('',isi.data, end='')
                 if isi.kanan:
                     isi.kanan.TampilkanPohon()
    
    def SisipkanData(isi, data):
        if isi.data:
            if data < isi.data:
                if isi.kiri is None:
                    isi.kiri = Node(data)
                else:
                    isi.kiri.SisipkanData(data)
            elif data > isi.data:
                if isi.kanan is None:
                    isi.kanan = Node(data)
                else:
                    isi.kanan.SisipkanData(data)
        else:
            isi.data = data
            
            
if __name__ == '__main__':
        print('=========================\nDemo Program Binary Tree')
        print('=========================')
        n = int(input('Masukkan banyaknya data: '))
        Akar = Node(n)
        for x in range(0,n):
            baca = int(input('Data ke -'+str(x+1)+': '))
            Akar.SisipkanData(baca)
        print('------------------------')
        print('Hasil Urutan Pohon: ')
        print('------------------------')
        Akar.TampilkanPohon()
exit()    