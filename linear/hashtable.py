class HashTable:
    def __init__(self):
        self.size = 100
        self.table = [ None for i in range(self.size)]
        
    def get_hash(self, key):
        h = 0
        for ch in key:
            h += ord(ch)
        return h % self.size

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.table[h] = value

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.table[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.table[h] = None

    def print_table(self):
        for key, value in enumerate(self.table):
            print(f"{key} : {value}")




if __name__ == "__main__":
    ht = HashTable()
    # ht._setitem__('march 6', 310)
    # ht._setitem__('march 7', 420)
    # ht._setitem__('march 8', 67)
    # ht._setitem__('march 9', 89)
    # # ht.priont_table()
    
    # ht._getitem__('march 6')
    ht['march 6'] = 310
    ht['march 7'] = 420
    ht['march 8'] = 67
    ht['march 9'] = 89
    print(ht['march 6'])
    
    
