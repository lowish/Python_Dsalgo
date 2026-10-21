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

    def delete(self, node, value):
        if node is None:
            return node
        
        if value < node.value:
            node.left = self.delete(node.left, value)
        elif value > node.value:
            node.right = self.delete(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Node with two children: Get the inorder successor (smallest in the right subtree)
            current = node.right
            while current.left is not None:
                current = current.left
            node.value = current.value
            node.right = self.delete(node.right, current.value)
            
        return node