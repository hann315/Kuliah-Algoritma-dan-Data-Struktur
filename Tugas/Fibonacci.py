def fibo_rekur(n):
    if n <= 1:
        return n
    else:
        return(fibo_rekur(n-1) + fibo_rekur(n-2))
    
angka = int(input('Masukkan angka: '))

if angka <= 0:
    print('Masukkan angka positif!')
else:
    print('Susunan Fibonacci-nya adalah:')
    for i in range(angka):
        print(fibo_rekur(i))
quit()