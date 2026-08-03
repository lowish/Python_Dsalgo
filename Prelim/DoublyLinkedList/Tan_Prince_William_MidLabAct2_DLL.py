class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
node1 = Node("Holy")
node2 = Node("Angel")
node3 = Node("University")
node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2

#Forward Doubly
print("Doubly Linked List (Forward):")
current = node1
while current is not None:
    print(current.data)
    current = current.next
#Backward Doubly
print("Doubly Linked List (Backward):")
current = node3
while current is not None:
    print(current.data)
    current = current.prev