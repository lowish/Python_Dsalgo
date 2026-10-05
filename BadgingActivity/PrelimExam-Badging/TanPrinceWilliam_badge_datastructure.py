#Prince William M. Tan
#BADGING
#WD-202

print("===== PYTHON DATA STRUCTURES EXPLORER =====\n")

#data types
int_val = 25
float_val = 89.75
string_val = "Prince William M. Tan"
boolean_val = True

print("DATA TYPES")
print("Integer Value:", int_val)
print("Float Value:", float_val)
print("String Value:", string_val)
print("Boolean Value:", boolean_val)

#this is a example of list
languages = ["Python", "Java", "C++"]

print("\nLIST")
print(languages)

#this is a example of tuple
devices = ("Keyboard", "Mouse", "Monitor")

print("\nTUPLE")
print(devices)

#this is a example of set
colors = {"Red", "Blue", "Green"}

print("\nSET")
print(colors)

#dictionary data type
student = {
    "id": 101,
    "name": "Peter",
    "course": "BSIT"
}

#dictionary
print("\nDICTIONARY")
print(student)
print("\nDictionary Keys")
print(student.keys())
print("\nDictionary Values")
print(student.values())
print("\nDictionary Items")
print(student.items())



print("\nLIST OPERATIONS")

print("\nOriginal List:")
print(languages)

#this will be add 
languages.append("JavaScript")
print("\nAfter append('JavaScript'):")
print(languages)

#this will be add another item
languages.insert(1, "PHP")
print("\nAfter insert(1, 'PHP'):")
print(languages)

#this will be remove
languages.remove("Java")
print("\nAfter remove('Java'):")
print(languages)

#search item
print("\nSEARCH ITEM")
search = input("Enter language to search: ")

if search in languages:
    print(search, "was found in the list.")
else:
    print(search, "was not found in the list.")
