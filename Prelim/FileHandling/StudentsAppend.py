file = open("students.txt", "a")

while True:
    name = input()
    if name == "END":
        break
    file.write(name + "\n")

file.close()