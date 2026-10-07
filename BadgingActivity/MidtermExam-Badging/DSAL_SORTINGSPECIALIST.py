class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def print_menu():
    print("\n==============================")
    print(" DSAL MIDTERM BADGING SYSTEM")
    print("==============================")
    print("1. Singly Linked List")
    print("2. Doubly Linked List")
    print("3. Circular Linked List")
    print("4. Exit")


def run_singly_linked_list():
    values = [10, 20, 30, 40, 50]
    head = tail = None

    for val in values:
        new_node = Node(val)
        if not head:
            head = tail = new_node
        else:
            tail.next = new_node
            tail = new_node
    
    print()
    print("Singly Linked List:")
    temp = head
    output = []
    while temp:
        output.append(str(temp.data))
        temp = temp.next
    print(" -> ".join(output))


def run_doubly_linked_list():
    values = ['A', 'B', 'C', 'D', 'E']
    head = tail = None

    for val in values:
        new_node = DNode(val)
        if not head:
            head = tail = new_node
        else:
            tail.next = new_node
            new_node.prev = tail
            tail = new_node

    print("\nForward Traversal:")
    temp = head
    forward_output = []
    while temp:
        forward_output.append(str(temp.data))
        temp = temp.next
    print(" <-> ".join(forward_output))

    print("\nBackward Traversal:")
    temp = tail
    backward_output = []
    while temp:
        backward_output.append(str(temp.data))
        temp = temp.prev
    print(" <-> ".join(backward_output))

    
def run_circular_linked_list():
    values = [100, 200, 300, 400]
    head = tail = None

    for val in values:
        new_node = Node(val)
        if not head:
            head = tail = new_node
        else:
            tail.next = new_node
            tail = new_node

    if tail:
        tail.next = head
    
    print()
    print("Circular Linked List:")
    temp = head
    output = []
    if head:
        while True:
            output.append(str(temp.data))
            temp = temp.next
            if temp == head:
                break
    print(" -> ".join(output) + " -> Back to Head")


def main():
    print()
    while True:
        print_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            run_singly_linked_list()
        elif choice == '2':
            run_doubly_linked_list()
        elif choice == '3':
            run_circular_linked_list()
        elif choice == '4':
            print()
            print("Program Terminated.")
            break
        else:
            print()
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()