class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        circular = Node(data)
        if not self.head:
            self.head = circular
            circular.next = self.head 
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = circular
            circular.next = self.head

    def display(self):
        if not self.head:
            print("The list is empty.")
            return
        print("Circular Linked List:")
        temp = self.head
        while True:
            print(temp.data)
            temp = temp.next
            if temp == self.head:
                break
CLL = CircularLinkedList()
CLL.append("Laus")
CLL.append("Deo")
CLL.append("Semper")
CLL.display()