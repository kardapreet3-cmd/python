#Q:CREATE A LIST OF 10 STUDENTS NAMES AND :A] ADD A NEW STUDENT
# B] REMOVE A STUDENT
# C]DISPLAY ALL STUDENTS
# Create a list of 10 student names
students = ["Aman", "Riya", "Karan", "Neha", "Rahul",
            "Priya", "Arjun", "Sneha", "Vikas", "Pooja"]

# Display original list
print("Original Student List:")
print(students)

# A] Add a new student
new_student = input("Enter the name of the new student: ")
students.append(new_student)

# B] Remove a student
remove_student = input("Enter the name of the student to remove: ")

if remove_student in students:
    students.remove(remove_student)
    print(remove_student, "removed successfully.")
else:
    print("Student not found.")

# C] Display all students
print("\nUpdated Student List:")
for student in students:
    print(student)