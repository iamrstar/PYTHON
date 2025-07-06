class node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
class DLL:
    def __init__(self):
        self.start = None
    def is_empty(self):
        return self.start == None
    def insert_at_start(self,data):
        n = node(None,data,self.start)
        if not self.is_empty():
            self.start.prev = n
        self.start = n
    def insert_at_last(self,data):
        if self.start is None:
            self.start = node(None,data,None)
            return
        temp = self.start
        while temp.next is not None:
            temp = temp.next
        n = node(temp,data,None)
        temp.next = n