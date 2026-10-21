class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    return root


def delete(root, data):
    if root is None:
        return None

    if data < root.data:
        root.left = delete(root.left, data)
    elif data > root.data:
        root.right = delete(root.right, data)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        successor = root.right
        while successor.left:
            successor = successor.left

        root.data = successor.data
        root.right = delete(root.right, successor.data)

    return root


def kth_smallest(root, k):
    values = []

    def inorder(node):
        if node is None:
            return
        inorder(node.left)
        values.append(node.data)
        inorder(node.right)

    inorder(root)

    if 1 <= k <= len(values):
        return values[k - 1]
    return None


root = None
print("Enter operations:")

while True:
    operation = input().split()

    if not operation:
        continue

    if operation[0] == "S":
        break
    elif operation[0] == "+":
        root = insert(root, int(operation[1]))
    elif operation[0] == "-":
        root = delete(root, int(operation[1]))
    elif operation[0] == "O":
        k = int(operation[1])
        result = kth_smallest(root, k)

        if result is not None:
            print(f"K-th smallest element ({k}): {result}")
        else:
            print("Element not found")