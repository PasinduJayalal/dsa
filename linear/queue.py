from collections import deque

class queue:
    def __init__(self):
        self._queue = deque()
        
    def enqueue(self, item):
        self._queue.appendleft(item)
        
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        return self._queue.pop()
    
    def is_empty(self):
        return len(self._queue) == 0
    
    def size(self):
        return len(self._queue)
    
    def print(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print(self._queue)
    
    
if __name__ == "__main__":
    q = queue()
    q.enqueue({
        "name": "John",
        "age": 25
    })
    q.enqueue({
        "name": "Jane",
        "age": 30
    })
    q.enqueue({
        "name": "Doe",
        "age": 35
    })
    print(q.size())
    q.print()
    q.dequeue()
    print(q.size())
    q.print()