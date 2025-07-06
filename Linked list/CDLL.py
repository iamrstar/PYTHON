class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class CDLL:
    def __init__(self, start=None):
        self.start = start

    def isempty(self):
        return self.start is None

    def insert_at_start(self, data):
        n = Node(item=data)
        if self.isempty():
            n.prev = n
            n.next = n
            self.start = n
        else:
            n.next = self.start
            n.prev = self.start.prev
            self.start.prev.next = n
            self.start.prev = n
            self.start = n

    def insert_at_last(self, data):
        n = Node(item=data)
        if self.isempty():
            n.prev = n
            n.next = n
            self.start = n
        else:
            n.next = self.start
            n.prev = self.start.prev
            self.start.prev.next = n
            self.start.prev = n

    def search(self, data):
        temp = self.start
        if temp is None:
            return None
        if temp.item == data:
            return temp
        temp = temp.next
        while temp != self.start:
            if temp.item == data:
                return temp
            temp = temp.next
        return None

    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(item=data)
            n.next = temp.next
            n.prev = temp
            temp.next.prev = n
            temp.next = n

    def print_list(self):
        temp = self.start
        if temp is not None:
            print(temp.item, end=' ')
            temp = temp.next
            while temp != self.start:
                print(temp.item, end=' ')
                temp = temp.next
            print()

    def delete_first(self):
        if self.start is None:
            return
        if self.start.next == self.start:
            self.start = None
        else:
            self.start.prev.next = self.start.next
            self.start.next.prev = self.start.prev
            self.start = self.start.next

    def delete_last(self):
         if self.start is None:
            return
         if self.start.next == self.start:
            self.start = None
         else:
             self.start.prev.prev.next = self.start
             self.start.prev = self.start.prev.prev
    def delete_item(self,data):
        if self.start is not None:
            temp = self.start
            if temp.item == data:
                self.delete_first()
            else:
                temp = temp.next
                while temp is not self.start: #jab tak temp firse start ko point nai  kareg TB TAK
                    if temp.item == data:
                        temp.next.prev = temp.prev
                        temp.prev.next = temp.next
                     
    def __iter__(self):
        return CDLLIterator(self.start)
     
class CDLLIterator:
    def __init__(self,start):
        
        self.current = start
        self.start = start
        self.count = 0
    def __iter__(self):
        return self
    def __next__ (self):
        if self.current is None:
            raise StopIteration
        if self.current == self.start and self.count == 1:
            raise StopIteration
        else:
          self.count = 1
          data = self.current.item 
        self.current = self.current.next
        return data

myList = CDLL()
myList.insert_at_start(10)
myList.insert_at_last(20)
myList.insert_at_last(30)
myList.insert_at_last(40)
myList.insert_after(myList.search(30),35)

for x in myList:
    print(x, end= ' ')
     

print ()
                
                
    
   
     


