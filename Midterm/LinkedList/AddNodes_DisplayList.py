class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__ (self):
        self.head = None
    
    def insert_end (self, data):
        if not self.head:
            self.head = Node(data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data)
        
    def display(self):
        elements, curr = [], self.head
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        elements.append("None")
        print(" -> ".join(elements))
items = input ("Enter values to insert (space-separated): ").strip().split()
ll = LinkedList()
for item in items:
    ll.insert_end(item)
    
print("\n--- Output ---")
ll.display()