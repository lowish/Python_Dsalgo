class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def display_forward(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        
        elements.append("None")
        print(" <-> ".join(elements))


def main():
    user_input = input("Enter space-separated values: ").strip()
    
    print("\n--- Output ---")
    
    if not user_input:
        print("None")
        return

    items = user_input.split()
    dll = DoublyLinkedList()

    for item in items:
        dll.insert_at_end(item)

    dll.display_forward()


if __name__ == "__main__":
    main()