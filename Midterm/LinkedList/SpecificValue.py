class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data)

    def insert_after_value(self, target, new_value):
        curr = self.head
        while curr and curr.data != target:
            curr = curr.next
        if curr:
            new_node = Node(new_value)
            new_node.next = curr.next
            curr.next = new_node

    def display(self):
        elements, curr = [], self.head
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        elements.append("None")
        print(" -> ".join(elements))

items = input("Enter initial list (space-separated): ").strip().split()
target = input("Enter value to insert after: ").strip()
new_val = input("Enter new value: ").strip()

ll = LinkedList()
for item in items:
    ll.append(item)

ll.insert_after_value(target, new_val)

print("\n--- Output ---")
ll.display()