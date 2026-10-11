class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create_node(message):
    return Node(input(message))


def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)


root = create_node("Enter Root Node: ")

root.left = create_node("Enter Left Child of Root: ")
root.right = create_node("Enter Right Child of Root: ")

root.left.left = create_node(
    "Enter Left Child of " + root.left.data + ": "
)

root.left.right = create_node(
    "Enter Right Child of " + root.left.data + ": "
)

root.right.left = create_node(
    "Enter Left Child of " + root.right.data + ": "
)

root.right.right = create_node(
    "Enter Right Child of " + root.right.data + ": "
)


print("\nIn-order Traversal:")
inorder(root)