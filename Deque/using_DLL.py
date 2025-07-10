class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0

    def is_empty(self): 
        return self.front == None
    def insert_front(self,data):
        n = Node(data)
        if self.is_empty():
            self.rear = n
            self.front = n
        else:
            n.next = self.front
            self.front.prev = n
            self.front = n
        self.item_count+=1
    def insert_rear(self,data):
        n = Node(data)
        if self.is_empty():
            self.rear = n
            self.front = n
        else:
            n.prev = self.rear
            self.rear.next = n
            self.rear = n
        self.item_count+=1
    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        elif self.front == self.rear :
            self.front = None
            self.rear = None
            self.item_count-=1
        else:
            self.front = self.front.next
            self.front = None
        self.item_count-=1
    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        elif self.front == self.rear :
            self.front = None
            self.rear = None
            self.item_count-=1
        else:
            self.rear = self.rear.prev
            self.rear = None
        self.item_count-=1
    def get_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            return self.front.item
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            return self.rear.item
    def  get_size(self):
        return self.item_count
dq = Deque()
dq.insert_front(10)
dq.insert_front(20)
dq.insert_front(70)
dq.insert_rear(30)
dq.insert_rear(40)
dq.insert_rear(90)
print(dq.get_front())
print(dq.get_rear())

