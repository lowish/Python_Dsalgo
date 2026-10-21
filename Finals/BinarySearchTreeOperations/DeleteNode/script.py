from binaryTree import BinaryTree

def main():
    test_case = int(input("Enter test case number (1 or 2): "))

    tree = BinaryTree()
    root = None

    if test_case == 1:
        for value in [3, 5, 8, 1, 6, 4, 7, 8]:
            root = tree.insert(root, value)

        print("Elements of the first tree:")
        tree.display_tree(root)

        root = tree.delete(root, 8)
        print("\nAfter deleting 8 from the first tree:")
        tree.display_tree(root)

    elif test_case == 2:
        for value in [10, 8, -1, 3, 12, 55, 2, 100]:
            root = tree.insert(root, value)

        print("Elements of the second tree:")
        tree.display_tree(root)

        root = tree.delete(root, 100)
        print("\nAfter deleting 100 from the second tree:")
        tree.display_tree(root)

    else:
        print("Invalid test case number.")

if __name__ == "__main__":
    main()