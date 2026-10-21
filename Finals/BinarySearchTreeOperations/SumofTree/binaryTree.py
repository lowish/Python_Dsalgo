class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def display_tree(self, node):
        if node:
            self.display_tree(node.left)
            print(node.value, end=" ")
            self.display_tree(node.right)

    def insert(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self.insert(node.left, value)
        elif value > node.value:
            node.right = self.insert(node.right, value)
        return node

    def sum_of_all_elements(self, node):
        if node is None:
            return 0
        return node.value + self.sum_of_all_elements(node.left) + self.sum_of_all_elements(node.right)