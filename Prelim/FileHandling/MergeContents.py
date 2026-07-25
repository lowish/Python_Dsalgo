print("Enter lines for the first file (end input with an empty line):")
with open("file1.txt", "w") as f1:
    while True:
        try:
            line = input()
            if line == "":
                break
            f1.write(line + "\n")
        except EOFError:
            break


print("Enter lines for the second file (end input with an empty line):")
with open("file2.txt", "w") as f2:
    while True:
        try:
            line = input()
            if line == "":
                break
            f2.write(line + "\n")
        except EOFError:
            break


with open("file1.txt", "r") as f1:
    lines1 = f1.read().splitlines()

with open("file2.txt", "r") as f2:
    lines2 = f2.read().splitlines()

combined_lines = lines1 + lines2


combined_lines.sort()


with open("merged.txt", "w") as merged_file:
    for line in combined_lines:
        merged_file.write(line + "\n")


print("Merged and sorted lines:")
with open("merged.txt", "r") as merged_file:
    print(merged_file.read(), end="")