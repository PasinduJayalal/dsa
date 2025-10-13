class BinarySearch:
    
    def __init__(self, number_list):
        self.number_list = sorted(number_list)
    
    
    def search(self, target):
        self.left = 0
        self.right = len(self.number_list) - 1
        self.mid = 0
        
        while self.left <= self.right:
            self.mid = (self.left + self.right) // 2
            self.mid_value = self.number_list[self.mid]
            
            if self.mid_value == target:
                return f"Found {target} at index {self.mid}"
            
            elif self.mid_value < target:
                self.left = self.mid + 1
            else:
                self.right = self.mid - 1
                
        return f"{target} not found in the list"
        
    
    
    def search_recursive(self, target, left, right):
        if left > right:
            return f"{target} not found in the list"
        
        mid = (left + right) // 2
        if mid >= len(self.number_list) or mid < 0:
            return f"{target} not found in the list"
        
        mid_value = self.number_list[mid]
        
        if mid_value == target:
            return f"Found {target} at index {mid}"
            
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
            
        return self.search_recursive(target, left, right)
    


if __name__ == "__main__":
    number_list = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    target = 15
    
    bs = BinarySearch(number_list)
    print(bs.search(target))
    print(bs.search(4))
    
    print(bs.search_recursive(target, 0, len(number_list)))
    