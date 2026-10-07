# Task 3: Student Examination Results
name = input("Student name: ")
coursework = float(input("Coursework mark (out of 30): "))
exam = float(input("Examination mark (out of 70): "))

total = coursework + exam
passed = total >= 40   # comparison operator gives True/False

print(f"Student: {name}")
print(f"Coursework: {coursework}")
print(f"Examination: {exam}")
print(f"Total Mark: {total}")
print(f"Passed: {passed}")
