class Node:
    def __init__(self,item = None, next = None):
        self.item = item
        self.next = next
class Stack:
    def __init__(self):
        self.start = None
        self.item_count = 0
    def is_empty(self):
        return self.start == None
    def push(self,data):
        n = Node(data,self.start)
        self.start = n
        self.item_count+=1
    def pop(self):
        if not self.is_empty():
            data = self.start.item
            self.start = self.start.next
            self.item_count-=1
            return data
        else:
            raise IndexError("stack is empty")
    def peek(self):
        if not self.is_empty():
          return self.start.item
        else:
            raise IndexError("stack is empty")
    def size(self):
        return self.item_count
    
s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("total element",s1.size())
print("top element",s1.peek())
print("pop element ",s1.pop())
    
          
        
