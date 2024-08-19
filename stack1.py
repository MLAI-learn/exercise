from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
def reverse_string(data):
        st=Stack()
        for char in data:
            st.push(char)

        strt=''
        while st.size()!=0:
            strt+=st.pop()
        return strt
        
       

        

            
        
    
if __name__=='__main__':
    print(reverse_string('We will conquere COVID-19'))
    print(reverse_string("I am the king"))
    
    