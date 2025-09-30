from collections import deque



class Stack:
    def __init__(self):
        self._stack = deque()

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self._stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self._stack[-1]

    def is_empty(self):
        return len(self._stack) == 0

    def size(self):
        return len(self._stack)

    def clear(self):
        self._stack.clear()
    
    def reverse(self, string):
        reversed_word = ''.join(reversed(string)) 
        self.push(reversed_word)
        return reversed_word

    
if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())
    print(s.peek())
    print(s.size())
    print(s.is_empty())
    s.push(4)
    print(s.pop())
    s.reverse("We will conquere COVID-19")
    print(s.peek())
    