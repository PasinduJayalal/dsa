import time
import threading
from collections import deque



class FoodOrderingSystem:
    def __init__(self):
        self._orders = deque()
        self._lock = threading.Lock()
        self._not_empty = threading.Condition(self._lock)
        
    def place_order(self, order):
        with self._not_empty:
            self._orders.appendleft(order)
            print(f"Order placed: {order}")
            self._not_empty.notify()
        time.sleep(0.5)
    
    def process_order(self):
        while True:
            with self._not_empty:
                while not self._orders:
                    print("No orders to process, waiting...")
                    self._not_empty.wait()
                order = self._orders.pop()
            if order is None:
                break
            print(f"Processing order: {order}")
            time.sleep(2)
        
    
            
if __name__ == "__main__":
    system = FoodOrderingSystem()
    worker = threading.Thread(target=system.process_order, daemon=True)
    worker.start()
    
    orders = [
        {"item": "Pizza", "quantity": 1},
        {"item": "Burger", "quantity": 2},
        {"item": "Sushi", "quantity": 3},
    ]
    
    for order in orders:
        system.place_order(order)
        
    system.place_order(None)  
    worker.join()
    
    
    
        
    