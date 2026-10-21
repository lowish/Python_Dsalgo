from binaryTree import BinaryTree

def main():
    tree = BinaryTree()
    root = None

    test_case = int(input("Enter a test case number: "))

    if test_case == 1:
        print("Test Case 1: Insertion and calculation of sum of leaf nodes")

        # Insert values into the tree
        values = [5, 3, 8, 1, 4, 7, 9]
        for value in values:
            root = tree.insert(root, value)

        # Insert more values into the tree
        more_values = [6, 2, 10]
        for value in more_values:
            root = tree.insert(root, value)

        # Insert negative values
        negative_values = [-5, -3]
        for value in negative_values:
            root = tree.insert(root, value)

        # Test with a larger tree
        larger_tree_values = [15, 12, 20, 11, 14, 18, 22]
        for value in larger_tree_values:
            root = tree.insert(root, value)

        # Sum of leaf nodes
        print(f"Sum of leaf nodes: {tree.sum_of_leaf_nodes(root)}")

    elif test_case == 2:
        print("Test Case 2: Insertion of more values and recalculation of sum of leaf nodes")
        new_values = [-5, -6, -10, 11, 105]
        for value in new_values:
            root = tree.insert(root, value)

        # Sum of leaf nodes
        print(f"Sum of leaf nodes: {tree.sum_of_leaf_nodes(root)}")

if __name__ == "__main__":
    main()