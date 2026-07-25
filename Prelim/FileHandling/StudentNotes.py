first_note = input("Enter first note: ")
with open("notes.txt", "w") as file:
    file.write(first_note + "\n")


second_note = input("Enter second note: ")
with open("notes.txt", "a") as file:
    file.write(second_note + "\n")


print("Full notes:")
with open("notes.txt", "r") as file:
    content = file.read()
    print(content, end="")