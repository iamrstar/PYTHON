class Node:
    def __init__(self, item=None, priority=None, next=None):
        self.item = item
        self.next = next
        self.priority = priority
class PriorityQueue:
    def __init__(self):
        self.start = None
        self.item_count = 0  

    def is_empty(self):
        return self.item_count == 0
    def push(self,data,priority):
        n = Node(data,priority)
        if not self.start or priority <self.start.priority:
            n.next = self.start
            self.start = n
        else:
            temp = self.start
            while temp.next and temp.next.priority <= priority:
                temp = temp.next
            n.next = temp.next
            temp.next = n
        self.item_count += 1
    def pop(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
             data = self.start.item
             self.start = self.start.next
             self.item_count -= 1
             return data       
    def size(self):
        return self.item_count
p = PriorityQueue()
p.push("A",2)
p.push("B",1)
p.push("C",3)
print(p.pop())
print(p.size()) 
       
            
         