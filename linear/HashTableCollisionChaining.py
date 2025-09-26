class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]
            
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
        if not found:
            self.arr[h].append((key,val))
        
    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        for index, element in enumerate(self.arr[arr_index]):
            if element[0] == key:
                print("del",index)
                del self.arr[arr_index][index]


if __name__ == "__main__":
    ht = HashTable()
    ht["march 6"] = 310
    ht["march 7"] = 420
    ht["march 8"] = 67
    ht["march 17"] = 63457
    print(ht.arr)    
    print(ht["march 6"])
    ht["march 6"] = 500
    print(ht["march 6"])
    print(ht.arr)
    del ht["march 6"]
    print(ht.arr)