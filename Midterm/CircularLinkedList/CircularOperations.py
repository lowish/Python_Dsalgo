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

    def delete_val(self, key):
        if not self.head:
            return

        curr = self.head
        if curr.data == key:
            if curr.next == self.head:
                self.head = None
                return
            
            last = self.head
            while last.next != self.head:
                last = last.next
            self.head = self.head.next
            last.next = self.head
            return
        prev = curr
        curr = curr.next
        while curr != self.head:
            if curr.data == key:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    def insert_after(self, target, data):

        curr = self.head
        while True:
            if curr.data == target:
                new_node = Node(data)
                new_node.next = curr.next
                curr.next = new_node
                return
            curr = curr.next
    def display(self):
        if not self.head:
            print("\n--- Output ---\n(back to head)")
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

cll = CircularLinkedList()

v1 = input("Insert value 1: ")
cll.append(v1)
v2 = input("Insert value 2: ")
cll.append(v2)
v3 = input("Insert value 3: ")
cll.append(v3)

val_to_delete = input("Value to delete: ")
cll.delete_val(val_to_delete)

target_val = input("Insert after which value? ")
new_val = input("New value to insert: ")
cll.insert_after(target_val, new_val)
cll.display()