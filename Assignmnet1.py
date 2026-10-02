# 1.Student Result Analyzer
# Create a Python program that accepts a student's:
# Name
# Marks in 3 subjects
# Calculate:
# Total marks
# Average marks
# Highest mark
# Lowest mark
# Use if-elif-else to assign:
# A+ → Average ≥ 90
# A → Average ≥ 80
# B → Average ≥ 70
# C → Average ≥ 60
# D → Average ≥ 40
# F → Below 40
# Display all information using f-strings.

student_name = input("Enter student name: ")
subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))
subject3 = float(input("Enter marks for subject 3: "))

total_marks = subject1 + subject2 + subject3
average_marks = total_marks / 3
highest_mark = max(subject1, subject2, subject3)
lowest_mark = min(subject1, subject2, subject3)

if average_marks >= 90:
    grade = "A+"
elif average_marks >= 80:
    grade = "A"
elif average_marks >= 70:
    grade = "B"
elif average_marks >= 60:
    grade = "C"
elif average_marks >= 40:
    grade = "D"
else:
    grade = "F"

print(f"Student Name: {student_name}")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks}")
print(f"Highest Mark: {highest_mark}")
print(f"Lowest Mark: {lowest_mark}")
print(f"Grade: {grade}")