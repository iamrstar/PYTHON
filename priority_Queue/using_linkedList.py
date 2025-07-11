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
        if self.is_empty():
            self.start = n
        else:
            
         