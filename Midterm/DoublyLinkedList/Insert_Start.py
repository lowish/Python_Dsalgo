class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node

    def display_forward(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        
        elements.append("None")
        print(" <-> ".join(elements))


def main():
    dll = DoublyLinkedList()

    for _ in range(3):
        val = input("Enter value to insert at start: ")
        dll.insert_at_start(val)

    print("\n--- Output ---")
    dll.display_forward()


if __name__ == "__main__":
    main()