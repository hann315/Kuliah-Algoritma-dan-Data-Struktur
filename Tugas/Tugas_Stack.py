"""
Pemrogram: Faisal A. F. Rahman
NIM: 21***11027
Nama berkas: Tugas_List.py
Tujuan : Membuat list untuk menambah data, dan mencari data
Interpreter : Python 3.10.4
Text Editor: Visual Code Studio
Operating System: Windows 11
"""

print('Nama: Faisal A. F. Rahman')
print('NIM: 21***11027\n')

print('=' * 60, '\n')

def cari(daftar_angka, cari_angka):
    for i in range(len(daftar_angka)):
        if daftar_angka[i] == cari_angka:
            return True
    return False

daftar_angka = [100, 50, 75, 25, 20, 45, 55, 30]

print('Sebelum ditambah data baru', daftar_angka) # Sebelum ditambah data baru

daftar_angka.append(9)
print('\nData yang masuk: ', 9)
print('Data saat ini: ', daftar_angka)

daftar_angka.append(10)
print('\nData yang masuk: ', 10)
print('Data saat ini: ', daftar_angka)

daftar_angka.append(200)
print('\nData yang masuk: ', 200)
print('Data saat ini: ', daftar_angka, '\n')

print('=' * 15, 'STACKING', '=' * 15)

stacking_1 = daftar_angka.pop()
print('\nData yang dikeluarkan:', stacking_1)
print('Data saat ini: ', daftar_angka) # Menghapus data terbaru. Data 200 dihapus.

stacking_2 = daftar_angka.pop() # Menghapus data terbaru. Data 10 dihapus.
print('\nData yang dikeluarkan: ', stacking_2)
print('Data saat ini: ', daftar_angka, '\n')

print('=' * 15, 'PENCARIAN DATA', '=' * 15)

cari_angka = int(input('\nMasukkan data yang akan dicari: ')) # Operasi mencari data

if cari(daftar_angka, cari_angka):
    print('\nData', cari_angka, 'ditemukan!')
else:
    print('\nData tidak ditemukan!')
exit()