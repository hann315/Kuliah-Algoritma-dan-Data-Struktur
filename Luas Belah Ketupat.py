print("Nama: Faisal A. F. Rahman\nNIM: 2130511027")

def cari_luas_belahketupat(p, q):  
    return ( ( p * q ) / 2)
p = float(input("Masukkan panjang Diagonal 1: "))
q = float(input("Masukkan panjang Diagonal 2: "))

print("Luas dari belah ketupat dengan panjang", p, "cm dan", q, "cm adalah",cari_luas_belahketupat(p, q), "cm3")