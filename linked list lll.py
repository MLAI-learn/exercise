class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_forward(self):
        if self.head is None:
            print('dll is empty')
            return

        itr = self.head
        dll = ''
        while itr:
            dll += str(itr.data) + '-->'
            itr = itr.next
        print(dll)

    def print_backward(self):
        if self.tail is None:
            print('dll is empty')
            return

        itr = self.tail
        rdll = ''
        while itr:
            rdll += str(itr.data) + '-->'
            itr = itr.prev
        print(rdll)

    def get_length(self):
        if self.head is None:
            return 0

        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_beginning(self, data):
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
            self.tail = node
            return

        node = Node(data, self.head, None)
        self.head.prev = node
        self.head = node

    def insert_at_end(self, data):
        if self.tail is None:
            node = Node(data, None, None)
            self.head = node
            self.tail = node
            return

        node = Node(data, None, self.tail)
        self.tail.next = node
        self.tail = node

if __name__ == '__main__':
    ll = Linked_list()
    
    ll.insert_at_beginning(3)
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(1)
    ll.print_forward()  # Output: 1-->2-->3-->
    ll.print_backward()  # Output: 3-->2-->1-->
