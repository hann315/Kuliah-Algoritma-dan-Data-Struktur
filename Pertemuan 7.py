import sys

KAMUS = {'one':'satu',
         'two':'dua',
         'three':'tiga',
         'four':'empat',
         'five':'lima',
         'six':'enam',
         'seven':'tujuh',
         'eight':'delapan',
         'nine':'sembilan',
         'ten':'sepuluh',
         #...
         }

def kamus():
    kata = input("Masukkan kata dalam bahasa Inggris: ")
    if not (kata in KAMUS.keys()):
        print("'%s' tidak ditemukan dalam kamus ini" % kata)
        sys.exit(1)
    print("Arti kata '%s' adalah '%s'" % (kata, KAMUS[kata]))
    
if __name__ == '__main__':
    kamus()
        