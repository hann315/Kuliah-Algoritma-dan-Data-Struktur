"""
Pemrogram: Faisal A. F. Rahman
NIM: 2130511027
Nama berkas: Tugas_List.py
Tujuan : Membuat list untuk menambah data, dan mencari data
Interpreter : Python 3.10.4
Text Editor: Visual Code Studio
Operating System: Windows 11
"""

print('Nama: Faisal A. F. Rahman')
print('NIM: 2130511027\n')

print('=' * 60, '\n')

def cari(daftar_angka, cari_angka):
    for i in range(len(daftar_angka)):
        if daftar_angka[i] == cari_angka:
            return True
    return False

# Sebelum data baru ditambahkan
daftar_angka = [100, 50, 75, 25, 20, 45, 55, 30]

print('Sebelum data ditambah: ', daftar_angka)

# Menambah data baru
daftar_angka.insert(0, 33)
daftar_angka.insert(10, 34)
daftar_angka.append(200)
print('\nSetelah data ditambah: ', daftar_angka, '\n')

# Mencari data
print('=' * 25, 'MENCARI ANTREAN', '=' * 27)

cari_angka = int(input('\nMasukkan data yang akan dicari: '))

if cari(daftar_angka, cari_angka):
    print('\nData', cari_angka, 'ditemukan!')
else:
    print('\nData tidak ditemukan!')
exit()