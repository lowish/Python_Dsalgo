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
        prev = None

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

user_input = input("Enter space-separated values: ")
val_delete = input("Enter value to delete: ")

cll = CircularLinkedList()
if user_input.strip():
    for val in user_input.split():
        cll.append(val)

cll.delete_val(val_delete)
cll.display()