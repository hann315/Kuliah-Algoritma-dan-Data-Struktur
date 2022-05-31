"""
Nama berkas: Pretemuan 8.py
Tujuan : Buat list untuk menambah data
Penterjemah : Python 3.7.9
Pemrogram: Faisal A. F. Rahman

"""

def main():
    list1 = [10, 20, 30]
    
    print("Sebelum ditambah")
    print("list1: ", list1)
    
    list1.append(40)
    list1.append(50)
    list1.insert(1, 15)
    list1.insert(1, 20)
    list1.extend((45, 55))
    
    print("\nSetelah ditambah")
    print("list1: ", list1)
    
if __name__ == "__main__":
    main()
quit()