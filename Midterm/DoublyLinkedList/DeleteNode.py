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

    def delete_by_value(self, value):
        current = self.head

        while current:
            if current.data == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                break
            current = current.next

    def display_forward(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next

        elements.append("None")
        print(" <-> ".join(elements))


def main():
    items_input = input("Enter list items (space-separated): ").strip()
    target_value = input("Enter value to delete: ").strip()

    dll = DoublyLinkedList()

    if items_input:
        for item in items_input.split():
            dll.insert_at_end(item)

    dll.delete_by_value(target_value)

    print("\n--- Output ---")
    dll.display_forward()


if __name__ == "__main__":
    main()