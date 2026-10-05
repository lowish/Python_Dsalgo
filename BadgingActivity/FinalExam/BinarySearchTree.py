#Prince William M. Tan
#WD-202
class Node:
    # NODE
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class BST:
    # Operations
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

    # Inorder: Left -> Root -> Right
    def inorder(self, root, res):
        if root:
            self.inorder(root.left, res)
            res.append(root.val)
            self.inorder(root.right, res)

    # Preorder: Root -> Left -> Right
    def preorder(self, root, res):
        if root:
            res.append(root.val)
            self.preorder(root.left, res)
            self.preorder(root.right, res)

    # Postorder: Left -> Right -> Root
    def postorder(self, root, res):
        if root:
            self.postorder(root.left, res)
            self.postorder(root.right, res)
            res.append(root.val)

    # Search for a value 
    def search(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self.search(root.left, key)
        return self.search(root.right, key)

def main():
    # Sequence of values to insert into the BST
    values = [50, 30, 70, 20, 40, 60, 80, 10, 35]
    
    # Build the tree
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

    # Search for 35
    search_key = 35
    found_node = bst.search(bst.root, search_key)
    print()
    if found_node:
        print(f"{search_key} found in the BST.")
    else:
        print(f"{search_key} not found in the BST.")

if __name__ == "__main__":
    main()