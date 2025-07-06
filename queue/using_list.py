class queue:
    def __init__(self): 
        self.items = []
        self.front = None
        self.rear = None
    def is_empty(self):
        return len(self.items)==0
    def enqueue(self,data):
      self.items.append(data)
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.items.pop(0)
    def get_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.items[0]
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.items[-1]
    def size(self):
        return len(self.items)
q1 = queue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.dequeue()
print(q1.get_front())
print(q1.get_rear())
print(q1.size())