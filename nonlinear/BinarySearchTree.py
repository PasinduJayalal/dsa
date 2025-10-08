class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
        
    def add_child(self, data):
        if self.data == data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)
    
    
    def search(self, val):
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
            
        if val> self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
    
    def in_order_traversal(self):
        elements = []
        
        if self.left:
            elements += self.left.in_order_traversal()
        
        elements.append(self.data)
            
        if self.right:
            elements += self.right.in_order_traversal()
        
        return elements
    
    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        
        if self.left:
            elements += self.left.pre_order_traversal()
    
        if self.right:
            elements += self.right.pre_order_traversal()
        
        return elements
    
    def post_order_traversal(self):
        elements = []
        
        if self.left:
            elements += self.left.post_order_traversal()
    
        if self.right:
            elements += self.right.post_order_traversal()
        
        elements.append(self.data)
        
        return elements
    
    def minimum(self):
        if self.left is None:
            return self.data
        return self.left.minimum()
    
    def maximum(self):
        if self.right is None:
            return self.data
        return self.right.maximum()
    
    
    def delete(self, val):
        if self.data > val:
            if self.left:
                self.left = self.left.delete(val)
        elif self.data < val:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            # max_val = self.left.maximum()
            # self.data = max_val
            # self.left = self.left.delete(max_val)
            min_val = self.right.minimum()
            self.data = min_val
            self.right = self.right.delete(min_val)
            
        return self
    
def build_tree(elements):
    root = BinarySearchTree(elements[0])
    
    for I in range(1, len(elements)):
        root.add_child(elements[I])
    
    return root

if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print("In order traversal gives a sorted list of elements:")
    print(numbers_tree.in_order_traversal())
    
    print(numbers_tree.search(20))
    print(numbers_tree.search(100))
    
    print("Minimum value in the tree is:", numbers_tree.minimum())
    print("Maximum value in the tree is:", numbers_tree.maximum())
    
    
    print("Pre order traversal gives:")
    print(numbers_tree.pre_order_traversal())
    
    print("Post order traversal gives:")
    print(numbers_tree.post_order_traversal())
    
    numbers_tree.delete(20)
    print("In order traversal after deleting 20:")
    print(numbers_tree.in_order_traversal())