# Prince William M. Tan
# Prelim Exam
# WD-202

studnumber = input("Enter Student Number: ")
studname = input("Enter Student Name: ")
cs = input("Enter Course: ")
prelim = input("Enter Preliminary Grade: ")

#data types
student = {
    "number": studnumber,
    "name": studname,
    "course": cs,
    "grade": prelim
}

#for spacing this print
print()

#display dictionary info
print("Keys:\n", student.keys())
print()
print("Values:\n", student.values())
print()
print("Items:\n", student.items())



#using for loop it gives you a 5 inputting subjects
subjects = []
print()
print("Enter 5 Subjects")
for i in range(1, 6):
    sub = input(f"Subject {i}: ")
    subjects.append(sub)



#add another subjects on the items
print()
print("Original List:\n", subjects)
new_sub = input("Enter subject to insert: ")
subjects.insert(2, new_sub)
print()

print("After Insert:\n", subjects)



#removing subject based on what you input
remove_sub = input("Enter subject to remove: ")
if remove_sub in subjects:
    subjects.remove(remove_sub)
    print()
    print("After Delete:", subjects)
else:
    print(f"Subject '{remove_sub}' not found in the list.")


#searching the subjects if found or not in the items you input
print()
search_query = input("Search Subject: ")
if search_query in subjects:
    print(f"'{search_query}' found in the list!")
else:
    print(f"'{search_query}' Subject Not Found")    