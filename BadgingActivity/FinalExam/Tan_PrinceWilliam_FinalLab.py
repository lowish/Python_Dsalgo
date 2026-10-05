#Prince William M. Tan
#WD-202

# PART I: BASIC SORTING ALGORITHMS


def selection_sort(arr):
    # Copy array to prevent in-place modification of the original data
    data = arr.copy()
    n = len(data)
    
    # Repeatedly find the minimum element in the unsorted portion and swap it to the front
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
        
    return data

def insertion_sort(arr):
    # Copy array to prevent in-place modification of the original data
    data = arr.copy()
    
    # Build sorted array one item at a time by shifting larger elements to the right
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        
    return data



# PART II: BINARY SEARCH TREE (BST)


class Node:
    # Node 
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class BST:
    # BST implementation
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current, key):
        if key < current.val:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert_recursive(current.left, key)
        elif key > current.val:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert_recursive(current.right, key)

    # Root -> Right
    def inorder(self, root, res):
        if root:
            self.inorder(root.left, res)
            res.append(root.val)
            self.inorder(root.right, res)

    #  Root -> Left -> Right
    def preorder(self, root, res):
        if root:
            res.append(root.val)
            self.preorder(root.left, res)
            self.preorder(root.right, res)

    #  Left -> Right -> Root
    def postorder(self, root, res):
        if root:
            self.postorder(root.left, res)
            self.postorder(root.right, res)
            res.append(root.val)

    # Search for a specific value
    def search(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self.search(root.left, key)
        return self.search(root.right, key)



# EXECUTION


def main():
    # PART I EXECUTION 
    user_input = input("Enter 10 integers:\n")
    numbers = list(map(int, user_input.split()))

    selection_result = selection_sort(numbers)
    insertion_result = insertion_sort(numbers)

    print("\nSelection Sort Result:")
    print(*selection_result)

    print("\nInsertion Sort Result:")
    print(*insertion_result)


    # PART II EXECUTION 
    values = [50, 30, 70, 20, 40, 60, 80, 10, 35]
    
    bst = BST()
    for val in values:
        bst.insert(val)

    inorder_res = []
    preorder_res = []
    postorder_res = []

    bst.inorder(bst.root, inorder_res)
    bst.preorder(bst.root, preorder_res)
    bst.postorder(bst.root, postorder_res)

    print("Inorder Traversal:")
    print(*inorder_res)

    print("\nPreorder Traversal:")
    print(*preorder_res)

    print("\nPostorder Traversal:")
    print(*postorder_res)

    search_key = 35
    found_node = bst.search(bst.root, search_key)
    print()
    if found_node:
        print(f"{search_key} found in the BST.")
    else:
        print(f"{search_key} not found in the BST.")

if __name__ == "__main__":
    main()