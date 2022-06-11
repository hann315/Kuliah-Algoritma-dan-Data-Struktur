Data = []

def Sequential_Search(data, cari):
    posisi = 0
    ketemu = False

    while posisi < len(data) and not ketemu:
        if data[posisi] == cari:
            ketemu = True
            print('Nama', cari, 'yang dicari ada di posisi ke', posisi+1)
        else:
            posisi += 1
    if ketemu == False:
        print('Maaf, nama', cari, 'yang dicari tidak ditemukan!')
    return ketemu

if __name__  == '__main__':
    try:
        n = int(input('Masukkan banyaknya nama: '))
        for i in range(0, n):
            Data.append([])
            Data[i].append(i)
            Data[i] = 0
            baca = str(input('Nama ke-'+str(i+1)+' = '))
            Data[i] = baca
        print('\nHasil: ', Data, '\n')
        Cari = str(input('Masukkan nama yang akan dicari: '))
        print()
        Sequential_Search(Data, Cari)
    except:
        print('Maaf, hanya masukan huruf alfabet!')
quit()