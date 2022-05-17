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