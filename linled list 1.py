class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next


class Linked_list:
    def __init__(self):
        self.head=None


    
    def printl(self):
        if self.head is None:
            print('ll is empty')
            return    

        itr=self.head
        llstr=''
        while itr:
            llstr+=str(itr.data) +'-->'
            itr=itr.next
        print(llstr)  


    def get_length(self):
        itr=self.head
        count=0
        while itr:
            count+=1
            itr=itr.next
        return count
        
    
    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node


    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        

        itr=self.head
        while itr.next:
            itr=itr.next

        node=Node(data,None)
        itr.next=node

    
    
    
    def insert_at(self,index,data):
        if index<0 or index> self.get_length():
            raise Exception('invalid index')
        
        if index==0:
            self.insert_at_begining(data)
            return
        

        itr=self.head
        count=0
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            count +=1
            itr=itr.next

    
    def remove_at(self,index):
        if index<0 or index>self.get_length():
            raise Exception('invalid index')
        

        if index==0:
            self.head=self.head.next
            return
        
        itr=self.head
        count=0
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            count+=1
            itr=itr.next
    

    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)


    def insert_after_value(self,data_after,data_to_insert):
        if self.head is None:
            return
        
        if self.head.data==data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return
        
        itr=self.head
        while itr:
            if itr.data==data_after:
                itr.next=Node(data_to_insert,itr.next)
                break
            itr=itr.next

    def remove_by_value(self,data):
        if self.head is None:
            return
        
        if self.head==data:
            self.head=self.head.next
            return

        itr=self.head
        while itr.next:
            if itr.next.data==data:
                itr.next=itr.next.next
                break
            itr=itr.next
       

if __name__=='__main__':
    ll = Linked_list()
    ll.insert_values([1,2,3,2])
    ll.printl()
    ll.insert_after_value(2,5) # insert apple after mango
    ll.printl()
    ll.remove_by_value(2) # remove orange from linked list
    ll.printl()
    ll.remove_by_value(2)
    ll.printl()
    ll.remove_by_value(1)
    ll.remove_by_value(5)
    
    ll.printl()
    
    







        


            
    

 




        

