#Prince William M. Tan
#WD-202
#midlabactivty1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def main():

    node1 = Node("Juan")
    node2 = Node("Maria")
    node3 = Node("Pedro")
    node4 = Node("Ana")
    node5 = Node("Carlos")    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5  
    current = node1    
    
    print("Waiting List:")
    while current is not None:
        print(current.data)
        current = current.next  

if __name__ == "__main__":
    main()