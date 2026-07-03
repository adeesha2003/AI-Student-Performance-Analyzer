print("="*40)
print("Student Performance Analyzer")
print("="*40)

# Get student name
student_name = input("Enter your name: ")

# Get student marks
student_marks = int(input("Enter your marks: "))

# Calculate grade
if student_marks >= 75:
    grade = "A"
elif student_marks >= 65:
    grade = "B"
elif student_marks >= 50:
    grade = "C"
else:
    grade = "F"

# Calculate status
if grade == "F":
    status = "Fail"
else:
    status = "Pass"

# Display results
print("="*40)
print("Student:", student_name)
print("Marks:", student_marks)
print("Grade:", grade)
print("Status:", status)
print("="*40)
