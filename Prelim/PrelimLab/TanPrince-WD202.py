#Prince William M. Tan
#WD-202
#DSALGO


grades = [85, 78, 90, 72, 88]

print("All Grades:", grades)

total = sum(grades)
count = len(grades)
average = total / count

print(f"The Average Grade is: {average}")

passing_grades = [grade for grade in grades if grade >= 75]

print("Grades Greater Than or Equal to 75:", passing_grades)