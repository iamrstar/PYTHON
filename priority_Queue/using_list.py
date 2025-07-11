class priority_queue():
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def push(self,data,priority):
        index = 0
        while index<len(self.items) and self.items[index] [1]<= priority:
            index += 1
        self.items.insert(index,(data,priority))
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is empty")
        else:
            return self.items.pop(0)[0]
    def size(self):
        return len(self.items)
p = priority_queue()
p.push("A",2)
p.push("B",1)
p.push("C",3)
print(p.pop())
print(p.size())  