class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
        def __init__(self):
            self.head = None
        def insert_start(self, data):
            new_node = Node(data)
            new_node.next= self.head
            self.head = new_node
        def display(self):
            current = self.head
            while current:
                print(f"{current.data} -> ", end="")
                current = current.next
            print("None")
        
linked_list = LinkedList()
        
for _ in range(3):
    val = input("Enter value: ")
    linked_list.insert_start(val)
            
print("\n--- Output ---")
linked_list.display()