# singly linked list
class node:
    def __init__(self,item=None, next=None):
        self.item = item
        self.next=next  

        class SLL:
          def __init__ (self , start=None):
             self.start = start

             def is_empty(self):
              
              return self.start == None
             
             def insert_at_start(self, data):
                 n = node(data,self. start)
                 self.start = n
                 self.start 

                 def insert_at_last(self , data):
                      n = node(data,self. next)  