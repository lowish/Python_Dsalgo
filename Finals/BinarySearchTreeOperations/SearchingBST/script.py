from binaryTree import BinaryTree

def main():
    test_case = int(input("Enter test case number (1 or 2): "))

    tree = BinaryTree()
    root = None

    if test_case == 1:
        # Test Case 1
        for value in [3, 5, 8, 1, 6, 4, 7, 8]:
            root = tree.insert(root, value)

        print("Elements of the first tree:")
        tree.display_tree(root)

        print("\n10 exists" if tree.search(root, 10) else "\n10 does not exist")

    elif test_case == 2:
        # Test Case 2
        for value in [10, 8, -1, 3, 12, 55, 2, 100]:
            root = tree.insert(root, value)

        print("Elements of the second tree:")
        tree.display_tree(root)

        print("\n100 exists" if tree.search(root, 100) else "\n100 does not exist")

    else:
        print("Invalid test case number.")

if __name__ == "__main__":
    main()