# Buat fungsi faktorial di sini

def faktorial(n):
    if n < 0:
        print('Angka yang dimasukkan adalah negatif!')
    elif n == 0:
        print('Faktorial dari 0 adalah 1.')
    else:
        f = 1
        for i in range (1,n+1):
            f = f * i
        return f

if __name__ == '__main__':
    n = int(input('Masukkan data: '))
    print('Faktorial dari ',n,'adalah ',faktorial (n))
quit()