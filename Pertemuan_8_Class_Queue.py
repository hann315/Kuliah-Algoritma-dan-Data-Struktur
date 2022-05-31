class Queue:
    def __init__(self):
        self.queue = list()
        
    def addtoq(self,isi_data):
        
        if isi_data not in self.queue:
            self.queue.insert(0, isi_data)
            return True, print(isi_data)
        return False
    
    def size(self):
        return len(self.queue)
    
if __name__ == "__main__":
    Antrian = Queue()
    print("Banyaknya data yang dimasukkan")
    print("------------------------------")
    Antrian.addtoq("Senin")
    Antrian.addtoq("Selasa")
    Antrian.addtoq("Rabu")
    Antrian.addtoq("Kamis")
    Antrian.addtoq("Jumat")
    print("\nSebanyak",Antrian.size(),"data")
quit()