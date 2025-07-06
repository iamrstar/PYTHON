class Node:
    # Define a class Node to describe a node of a singly linked list
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class SLL:
    # Define a class SLL to implement a singly linked list
    def __init__(self, start=None):
        self.start = start 
    
    # Define a method to check if the linked list is empty
    def is_empty(self):
        return self.start is None

    # Insert an element at the beginning of the linked list
    def insert_at_start(self, data):
        n = Node(data, self.start)
        self.start = n

    # Insert an element at the end of the linked list
    def insert_at_last(self, data):
        n = Node(data)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.start = n

    # Define a method search() to find the node with specified element value
    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None

    # Define a method insert_after() to insert a new node after a given node of the list
    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(data, temp.next) 
            temp.next = n 
    
    # Define a method to delete the first node
    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next

    # Define a method to delete the last node
    def delete_last(self):
        if self.start is None:
            return
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None

    # Define a method delete_item() to delete a specific node
    def delete_item(self, data):
        if self.start is None:
            return
        elif self.start.item == data:
            self.start = self.start.next
        else:
            temp = self.start
            while temp.next is not None:
                if temp.next.item == data:
                    temp.next = temp.next.next
                    break
                temp = temp.next
    
    # Define a method to print the list
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=' -> ')
            temp = temp.next
        print("None")
#implement iterator for SLL to access all the elements of the list in a sequence
    def __iter__(self):
       return SLLIterator(self.start)
class SLLIterator:
    def __init__(self, start):
        self.cureent=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.cureent:
            raise StopIteration
        data = self.cureent.item
        self.cureent=self.cureent.next
        return data
# Driver code
myList = SLL()
myList.insert_at_start(20)
myList.insert_at_start(10)
myList.insert_at_last(30)
myList.insert_after(myList.search(20), 25)

myList.delete_item(30)
myList.print_list()

for x in myList:
    print(x, end='->')
 