from binaryTree import BinaryTree

def main():
    tree = BinaryTree()
    root = None

    test_case = int(input("Enter a test case number: "))

    if test_case == 1:
        print("Test Case 1: Insertion and preorder traversal")
        # Insert values into the tree
        values = [5, 3, 8, 1, 4, 7, 9]
        for value in values:
            root = tree.insert(root, value)

        print("Preorder Traversal of the tree:")
        tree.preorder_traversal(root)
        print()

    elif test_case == 2:
        print("Test Case 2: Insertion of more values and preorder traversal")
        # Insert more values into the tree
        more_values = [6, 2, 10]
        for value in more_values:
            root = tree.insert(root, value)

        print("Preorder Traversal after inserting more values:")
        tree.preorder_traversal(root)
        print()

    elif test_case == 3:
        print("Test Case 3: Insertion of negative values and preorder traversal")
        # Insert negative values
        negative_values = [-5, -3]
        for value in negative_values:
            root = tree.insert(root, value)

        print("Preorder Traversal after inserting negative values:")
        tree.preorder_traversal(root)
        print()

    elif test_case == 4:
        print("Test Case 4: Larger tree and preorder traversal")
        # Test with a larger tree
        larger_tree_values = [15, 12, 20, 11, 14, 18, 22]
        for value in larger_tree_values:
            root = tree.insert(root, value)

        print("Preorder Traversal of a larger tree:")
        tree.preorder_traversal(root)
        print()

if __name__ == "__main__":
    main()