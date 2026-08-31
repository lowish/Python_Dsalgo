class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_by_value(self, target):
        if not self.head:
            return

        if self.head.data == target:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.data != target:
            current = current.next


        if current.next:
            current.next = current.next.next

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        elements.append("None")
        print(" -> ".join(elements))


def main():
    items_input = input("Enter list items (space-separated): ").strip().split()
    target_val = input("Enter value to delete: ").strip()

    ll = LinkedList()
    for item in items_input:
        ll.append(item)

    ll.delete_by_value(target_val)

    print("\n--- Output ---")
    ll.display()


if __name__ == "__main__":
    main()