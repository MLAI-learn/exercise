class fib:
    def __init__(self,lim) :
        self.prev=0
        self.next=1
        self.n=1
        self.lim=lim


    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n<self.lim:
            result=self.prev+self.next
            self.prev=self.next
            self.next=result
            self.n+=1
            return result
        else:
            raise StopIteration
         
        
    

f=fib(9)

while True:
    try:
       print(next(f))
    except StopIteration:
        break







