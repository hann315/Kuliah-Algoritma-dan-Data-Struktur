"""
Pemrogram: Faisal A. F. Rahman
NIM: 2130511027
Nama berkas: Tugas_List.py
Tujuan : Membuat list untuk menambah data, dan mencari data
Interpreter : Python 3.10.4
Text Editor: Visual Code Studio
Operating System: Windows 11
"""

from collections import deque

print('Nama: Faisal A. F. Rahman')
print('NIM: 2130511027\n')

print('=' * 68, '\n')

def cari(daftar_antrian, cari_angka):
    for i in range(len(daftar_antrian)):
        if daftar_antrian[i] == cari_angka:
            return True
    return False

daftar_antrian = deque([100, 50, 75, 25, 20, 45, 55, 30])
print('Antrean saat ini: ', daftar_antrian, '\n')

print('=' * 25, 'MENAMBAH ANTREAN', '=' * 25)

# Menambahkan data antrean baru
daftar_antrian.append(200)
print('\nAntrean masuk: ', 200)
print('Antrean saat ini: ', daftar_antrian)

daftar_antrian.append(300)
print('\nAntrean masuk: ', 300)
print('Antrean saat ini: ', daftar_antrian)

daftar_antrian.append(400)
print('\nAntrean masuk: ', 400)
print('Antrean saat ini: ', daftar_antrian, '\n')

print('=' * 25, 'MENGHAPUS ANTREAN', '=' * 25)

# Menghapus data antrean di depan atau sebelah kiri
hapus_data_1 = daftar_antrian.popleft()
print('\nAntrean yang dihapus: ', hapus_data_1)
print('Antrean saat ini: ', daftar_antrian)

hapus_data_2 = daftar_antrian.popleft()
print('\nAntrean yang dihapus: ', hapus_data_2)
print('Antrean saat ini: ', daftar_antrian)

hapus_data_3 = daftar_antrian.popleft()
print('\nAntrean yang dihapus: ', hapus_data_3)
print('Antrean saat ini: ', daftar_antrian, '\n')

# Mencari data antrean

print('=' * 25, 'MENCARI ANTREAN', '=' * 27)

cari_angka = int(input('\nMasukkan data yang akan dicari: ')) # Operasi mencari data

if cari(daftar_antrian, cari_angka):
    print('\nData', cari_angka, 'ditemukan!')
else:
    print('\nData tidak ditemukan!')
exit()