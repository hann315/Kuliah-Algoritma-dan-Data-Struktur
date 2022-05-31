class Node:
    
    def __init__(isidata, data):
        isidata.kiri = None
        isidata.Kanan = None
        isidata.data = data
        
    def TampilkanPohoh(isidata):
        print(isidata.data)
        
if __name__ == '__main__':
    root = Node(100)
    root.TampilkanPohon()