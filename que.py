import time
import threading

from collections import deque



class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)

food_order=Queue()

def place_order(orders):
    for order in orders:
        print('placing order for:',order)
        food_order.enqueue(order)
        time.sleep(0.5)

def serve_order():
    time.sleep(1)
    while food_order.size()!=0:
        order=food_order.dequeue()
        print('serving:',order)
        time.sleep(2)
if __name__ == '__main__':
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target=place_order, args=(orders,))
    t2 = threading.Thread(target=serve_order)

    t1.start()
    t2.start()








