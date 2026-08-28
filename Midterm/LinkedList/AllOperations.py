class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        if not self.head:
            self.head = Node(data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data)

    def insert_after_value(self, target, new_val):
        curr = self.head
        while curr and curr.data != target:
            curr = curr.next
        if curr:
            new_node = Node(new_val)
            new_node.next = curr.next
            curr.next = new_node

    def delete_by_value(self, target):
        if not self.head:
            return
        if self.head.data == target:
            self.head = self.head.next
            return
        curr = self.head
        while curr.next and curr.next.data != target:
            curr = curr.next
        if curr.next:
            curr.next = curr.next.next

    def display(self):
        elements, curr = [], self.head
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        elements.append("None")
        print(" -> ".join(elements))

ll = LinkedList()

ll.insert_at_start(input("Insert at start: ").strip())
ll.insert_at_start(input("Insert at start: ").strip())

ll.insert_at_end(input("Insert at end: ").strip())
ll.insert_at_end(input("Insert at end: ").strip())

target = input("Insert after value: ").strip()
new_val = input("New value to insert after target: ").strip()
ll.insert_after_value(target, new_val)

delete_val = input("Enter value to delete: ").strip()
ll.delete_by_value(delete_val)

print("\n--- Output ---")
ll.display()