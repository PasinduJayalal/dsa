from collections import deque


class BinaryQueue:
    def __init__(self):
        self._queue = deque()
        
    def enqueue(self, item):
        self._queue.appendleft(item)
        
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        return self._queue.pop()
    
    def is_empty(self) -> bool:
        return len(self._queue) == 0
    
    def size(self) -> int:
        return len(self._queue)
    
    def print(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print(self._queue)
        
    def front(self):
        if self.is_empty():
            raise IndexError("front from an empty queue")
        return self._queue[-1]
    

def binary_count(n):
    bq = BinaryQueue()
    bq.enqueue("1")
    for i in range(n):
        s = bq.front()
        bq.dequeue()
        print(s) 
        
        bq.enqueue(s + "0")
        bq.enqueue(s + "1")


if __name__ == "__main__":
    num = 10
    binary_count(num)
    
       
        