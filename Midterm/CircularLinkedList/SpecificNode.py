class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        curr.next = new_node
        new_node.next = self.head

    def insert_after(self, target, data):
        if not self.head:
            return

        curr = self.head
        while True:
            if curr.data == target:
                new_node = Node(data)
                new_node.next = curr.next
                curr.next = new_node
                return
            curr = curr.next
            if curr == self.head:
                break

    def display(self):
        if not self.head:
            return
        
        print("\n--- Output ---")
        curr = self.head
        res = []
        while True:
            res.append(f"{curr.data} -> ")
            curr = curr.next
            if curr == self.head:
                break
        res.append("(back to head)")
        print("".join(res))

user_input = input("Enter space-separated values: ")
target_val = input("Insert after which value? ")
new_val = input("Enter new value to insert: ")

cll = CircularLinkedList()
if user_input.strip():
    for val in user_input.split():
        cll.append(val)

cll.insert_after(target_val, new_val)
cll.display()