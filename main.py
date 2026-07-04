print("="*40)
print("Student Performance Analyzer")
print("="*40)

# Function to calculate grade
def calculate_grade(marks):
    if marks >= 75:
        return "A"
    elif marks >= 65:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "F"
    
#Function to calculate pass/fail status
def calculate_status(grade):
    if grade == "F":
        return "Fail"
    else:
        return "Pass"

# Get student name
name = input("Enter your name: ")

# Get student marks
while True:
    marks = int(input("Enter your marks: "))
    if 0 <= marks <= 100:
        break
    else:
        print("Invalid marks. Please enter a value between 0 and 100.")

#Calculate grade
grade = calculate_grade(marks)
status = calculate_status(grade)

# Display results
print("="*40)
print("Student Report")
print("="*40)
print("Student:", name)
print("Marks:", marks)
print("Grade:", grade)
print("Status:", status)
