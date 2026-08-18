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

    def display_backward(self):
        current = self.tail
        elements = []
        while current:
            elements.append(current.data)
            current = current.prev

        elements.append("None")
        print(" <-> ".join(elements))


def main():
    user_input = input("Enter values (space-separated): ").strip()

    dll = DoublyLinkedList()

    if user_input:
        for item in user_input.split():
            dll.insert_at_end(item)

    print("\n--- Output ---")
    dll.display_backward()


if __name__ == "__main__":
    main()