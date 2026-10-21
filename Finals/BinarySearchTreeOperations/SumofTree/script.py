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

        sum1 = tree.sum_of_all_elements(root)
        print("\nSum of all elements in the first tree:", sum1)

    elif test_case == 2:
        for value in [10, 8, -1, 3, 12, 55, 2, 100]:
            root = tree.insert(root, value)

        print("Elements of the second tree:")
        tree.display_tree(root)

        sum2 = tree.sum_of_all_elements(root)
        print("\nSum of all elements in the second tree:", sum2)

    else:
        print("Invalid test case number.")

if __name__ == "__main__":
    main()