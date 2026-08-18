class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_start(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

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

    def display_backward(self):
        current = self.tail
        elements = []
        while current:
            elements.append(current.data)
            current = current.prev
        elements.append("None")
        print(" <-> ".join(elements))


def main():
    dll = DoublyLinkedList()

    val1 = input("Insert at start: ")
    dll.insert_at_start(val1)
    val2 = input("Insert at start: ")
    dll.insert_at_start(val2)
    val3 = input("Insert at end: ")
    dll.insert_at_end(val3)
    val4 = input("Insert at end: ")
    dll.insert_at_end(val4)
    delete_val = input("Enter value to delete: ")
    dll.delete_by_value(delete_val)
    print("\n--- Output (Forward) ---")
    dll.display_forward()
    print("\n--- Output (Backward) ---")
    dll.display_backward()

if __name__ == "__main__":
    main()