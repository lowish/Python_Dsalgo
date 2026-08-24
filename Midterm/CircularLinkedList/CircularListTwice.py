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

    def display_twice(self):
        if not self.head:
            return
        
        print("\n--- Output ---")
        curr = self.head
        res = []
        laps = 0
        
        while laps < 2:
            res.append(f"{curr.data} -> ")
            curr = curr.next
            if curr == self.head:
                laps += 1
                
        res.append("(looped twice)")
        print("".join(res))

user_input = input("Enter space-separated values: ")

cll = CircularLinkedList()
if user_input.strip():
    for val in user_input.split():
        cll.append(val)

cll.display_twice()