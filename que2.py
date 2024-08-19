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
    


def convert_to_binary(s):
    num=Queue()
    for i in range(1,s+1):
        c=format(i,'b')
        num.enqueue(c)
        
        
        print(num.dequeue())
    
    

        
        

if __name__=='__main__':
   
    convert_to_binary(10)






