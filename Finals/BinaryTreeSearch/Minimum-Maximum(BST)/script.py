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


def find_min(root):
    while root.left:
        root = root.left
    return root.data


def find_max(root):
    while root.right:
        root = root.right
    return root.data


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

if root:
    print("Minimum element:", find_min(root))
    print("Maximum element:", find_max(root))