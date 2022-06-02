"""
Name: Faisal A. F. Rahman
NIM: 21***11027
Purposes: Add new data, search data, and show added data from DB.
Text Editor: Visual Code Studio
Interpreter: Python 3.10.4
Operating System: Windows 11
"""

nama = []
nomor_telp = []
hobi = []
umur = []
No_Induk_Mahasiswa = []

def menu_utama():
    print('''
__________ MENU __________
    1. Data Baru
    2. Cari Data
    3. Tampilkan Data
    ''')
    pilih_menu = input('Masukkan menu: ')
    if pilih_menu == '1':
        menu_daftar_data()
    elif pilih_menu == '2':
        menu_cari_data()
    elif pilih_menu == '3':
        menu_tampilkan_data
    else:
        print('\nPilihan tersebut tidak ada!')
        menu_utama()