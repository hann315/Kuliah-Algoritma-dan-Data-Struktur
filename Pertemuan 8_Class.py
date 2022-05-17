class Stack:
    
    def __init__(self):
        self.stack = []
        
        
    def add(self, isi_data):
        if isi_data not in self.stack:
            self.stack.append(isi_data)
            return True
        else:
            return False
        
    def peek(self):
        return self.stack[-1]
    
if __name__ == '__main__':
    Tumpukan = Stack()
    Tumpukan.add("Senin")
    Tumpukan.add("Selasa")
    Tumpukan.peek()
    print(Tumpukan.peek())
    Tumpukan.add("Rabu")
    Tumpukan.add("Kamis")
    print(Tumpukan.peek())
    Tumpukan.add("Jumat")
    Tumpukan.add("Sabtu")
    print(Tumpukan.peek())
quit()