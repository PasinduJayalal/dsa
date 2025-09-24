
class Node:
 def __init__(self, data = None, next=None):
     self.data = data
     self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
    
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
            
        print(llstr)
        
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
            
        itr.next = Node(data, None)
        
    def insert_list(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
            
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            print("invalid Index")
            
        if index == 0:
            self.head = self.head.next
            
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
            
    def insert_at(self, index , data):
        
        if index < 0 or index >= self.get_length():
            print("invalid Index")
            
            
        if index == 0:
            self.insert_at_beginning(data)
        
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
            
            
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            itr = itr.next
        

    def remove_by_value(self, data):
        # Remove first node that contains data
        itr = self.head
        while itr:
            if itr.data == data:
                self.head.next = itr.next
                break
            itr = itr.next
        


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(15)
    ll.print()
    ll.insert_at_end(20)
    ll.print()
    ll.insert_list(["banana", "mango", "grapes", "orange"])
    ll.print()
    print(f"Length of linked list: {ll.get_length()}")
    ll.remove_at(2)
    ll.print()
    ll.insert_at(2,"grapes")
    ll.print()
    ll.insert_after_value("orange", "apple")
    ll.print()
    ll.remove_by_value("mango")
    ll.print()