# 1. Create the Student Profile Dictionary
student_profile_tan = {
    "no": "21039996",
    "name": "Prince Tan",
    "course": "Web Development",
    "section": "WD-202",
    "age": 19,
    "email": "pmtan@student.hau.edu",
}

# 2. Display all info
print("--- Student Profile ---")
print(student_profile_tan["no"])
print(student_profile_tan["name"])
print(student_profile_tan["course"])
print(student_profile_tan["section"])
print(student_profile_tan["age"])
print(student_profile_tan["email"])

# 3. Add a new key "status" with value "Regular"
student_profile_tan["status"] = "Regular"

# 4. Update my age
student_profile_tan["age"] +=1

# 5. Delete the "email" key
del student_profile_tan["email"]
