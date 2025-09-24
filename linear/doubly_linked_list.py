class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self, data):
        if self.head is None:
            node = Node(data, None , None)
            self.head = node
            return
        node = Node(data, self.head, None)
        self.head.prev = node
        self.head = node
        
    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data , None , None)
            self.head = node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        node = Node(data , None , itr)
        itr.next = node
    
    def remove_by_value(self, data):
        if self.head.data == data:
            self.head = self.head.next      # step A: move head forward
        if self.head:                   # step B: clear back link if list not empty
            self.head.prev = None
        
        itr = self.head.next
        while itr:
            if itr.data == data:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                return
            itr = itr.next
    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' <=> '
            itr = itr.next
        print(llstr)
        
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_beginning(5)
    dll.insert_at_beginning(10)
    dll.insert_at_beginning(15)
    dll.print()
    dll.insert_at_end(20)
    dll.insert_at_end(25)
    dll.print()
    # dll.remove_by_value(15)
    dll.print()
    dll.insert_at_beginning(19)
    dll.print()