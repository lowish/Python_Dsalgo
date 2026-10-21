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


def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


root = None
print("Enter operations:")

while True:
    operation = input().split()

    if not operation:
        continue

    if operation[0] == "0":
        break
    elif operation[0] == "+":
        root = insert(root, int(operation[1]))
    elif operation[0] == "-":
        root = delete(root, int(operation[1]))

print("Inorder traversal:")
inorder(root)
print()