if __name__ == '__main__':
    print('Gabungan')
    print('--------')
    print('1. Contoh Sekuensial')
    print('2. Contoh Percabangan')
    print('3. Pengulangan')
    print('4. Selesai')
    print('-------------------------')
    pilih = int(input('Silahkan Pilih: '))
    print()
    if pilih == 1:
        print('Anda memilih Sekuensial \n')
        x = int(input('Masukan Angka X: '))
        y = int(input('Masukan Angka Y: '))
        print('Hasil penjumlahan: ',x+y)
    elif pilih == 2:
        x = int(input('Masukan Angka X: '))
        y = int(input('Masukan Angka Y: '))
        print('Hasil perkalian',x*y)
        if x<=y: print('')
        else: print('Y lebih kecil dari pada X')
    elif pilih == 3:
        i = 1
        n = int(input('Masukan Angka N: '))
        print('Pakai While - Do \n')
        while i <= n:
            print('No: ',i,'Teks While - Do dicetak sebanyak: ',i,'kali')
            i += 1 # sama dengan 1 + 1 = 1
        print()
        print('Pakai For - Do \n')
        for i in range(1, n):
            print('No: ',i,'Teks For - Do dicetak sebanyak: ',i,'kali')
    else:
        print()
        print('Anda memilih menu Selesai.\nTerima kasih telah mencoba program ini...')
quit()