class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [ None for i in range(self.MAX)]
    
    
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def get_prob_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0, index)]
    
    def find_slot(self, key, index):
        empty_slot = self.get_prob_range(index)    
        for empty in empty_slot:
            if self.arr[empty] is None or self.arr[empty][0] == key:
                return empty
        raise Exception("Hashmap full")
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key,val)
            return
        else:
            slot = self.find_slot(key, h)
            self.arr[slot] = (key,val)
            
    def __getitem__(self, key):
        h = self.get_hash(key)
        for hk in self.get_prob_range(h):
            if self.arr[hk] is None:
                return None
            if self.arr[hk][0] == key:
                return self.arr[hk][1]
        
    def __delitem__(self, key):
        h = self.get_hash(key)
        for hk in self.get_prob_range(h):
            if self.arr[hk] is None:
                return
            if self.arr[hk][0] == key:
                self.arr[hk] = None
                new_hk = (hk + 1) % self.MAX
                while self.arr[new_hk] is not None:
                    new_key, new_val = self.arr[new_hk]
                    self.arr[new_hk] = None
                    self.__setitem__(new_key, new_val)
                    new_hk = (new_hk + 1) % self.MAX
                return
               
            
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
    print(ht["march 17"])
