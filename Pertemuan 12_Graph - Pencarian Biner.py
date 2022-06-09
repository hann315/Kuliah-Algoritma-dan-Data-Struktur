Data = []

def bubblesort(data):
    for i in range(0, len(data)-1):
        print('Tahap %d: ' %(i+1), end='')
        for j in range(len(data)-1, i, -1):
            if data[j] < data[j  - 1]:
                data[j]. data[j - 1] = data[j - 1], data[j]
        print(data)

def Cari_Biner(data, cari):
    awal = 0
    akhir = len(data)-1
    ketemu = False

    while(awal <= akhir and not ketemu):
        partisi = (awal + akhir) // 2

        if data[partisi] == cari:
            ketemu = True
            print('Angka', cari, 'yang dicari ada di lokasi ke-', partisi + 1)
        else:
            if cari < data[partisi]:
                akhir = partisi -1
            else:
                awal = partisi + 1