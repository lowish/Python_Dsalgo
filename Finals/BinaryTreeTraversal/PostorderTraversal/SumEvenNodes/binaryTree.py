class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def insert(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self.insert(node.left, value)
        elif value > node.value:
            node.right = self.insert(node.right, value)
        return node

    def sum_of_even_nodes(self, node):
        # Implement me!
        if node is None:
            return 0

        current_sum = node.value if node.value % 2 == 0 else 0
        return current_sum + self.sum_of_even_nodes(node.left) + self.sum_of_even_nodes(node.right)