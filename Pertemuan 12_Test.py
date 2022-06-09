Data = []

def Pencarian_Beruntun(data, cari):
    posisi = 0
    ketemu = False

    while posisi < len(data) and not ketemu:
        if data[posisi] == cari:
            ketemu = True
            print('Angka:', cari, 'yang dicari ada di lokasi ke', posisi+1)
        else:
            posisi += 1
    if ketemu == False:
        print('Angka', cari, 'tidak ditemukan!')
    return ketemu

if __name__ == '__main__':
    try:
        n = int(input('Masukkan banyaknya angka: '))
        for i in range(0, n):
            Data.append([])
            Data[i].append(i)
            Data[i] = 0
            baca = int(input('Angka ke-'+str(i+1)+' = '))
            Data[i] = baca
        print('\nHasil: ', Data)
        Cari = int(input('\nMasukkan angka yang akan dicari: ', '\n'))
        Pencarian_Beruntun(Data, Cari)
    except:
        print('Maaf, angka yang dimasukkan harus angka bulat!')
quit()