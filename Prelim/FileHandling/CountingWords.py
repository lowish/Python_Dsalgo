paragraph = input("Enter your paragraph: ")

with open("essay.txt", "w") as file:
    file.write(paragraph)

with open("essay.txt", "r") as file:
    content = file.read()

words = content.split()
print("Word count:", len(words))