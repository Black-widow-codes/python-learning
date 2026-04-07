class Student:
    # Constructor - Initializes a Student object with all attributes
    # Method_1 
    def __init__(self, Name, ID, Age, Department, Course, Term):
        # Store the student's name
        self.Name = Name
        # Store the student's ID number
        self.ID = ID
        # Store the student's age
        self.Age = Age
        # Store the student's department
        self.Department = Department
        # Store the course name
        self.Course = Course
        # Store the term/semester
        self.Term = Term

    # Method_2 - Displays all student information
    def display(self):
        # Print student name
        print(f'Name: {self.Name}')
        # Print student ID
        print(f'ID: {self.ID}')
        # Print student age
        print(f'Age: {self.Age}')
        # Print student department
        print(f'Department: {self.Department}')
        # Print course name
        print(f'Course: {self.Course}')
        # Print term/semester
        print(f'Term: {self.Term}')

# ===== FIRST VERSION (ORIGINAL) - COMMENTED OUT =====
# #Object_1
# Student_1 = Student('Bryan', 202020, 20, 'SETAS', 'Comp100', 'Winter')
# print(Student_1.Name)
# print(Student_1.ID)
# print(Student_1.Age)
# print(Student_1.Department)
# print(Student_1.Course)
# print(Student_1.Term)
#
# #Object_2
# Student_2 = Student('Alex', 303030, 21, 'Business', 'Accounts', 'Summer')
# print(Student_2.Name)
# print(Student_2.ID)
# print(Student_2.Age)
# print(Student_2.Department)
# print(Student_2.Course)
# print(Student_2.Term)
#
# #Object_3
# Student_3 = Student('Bob', 101010, 26, 'Arts', 'History', 'Fall')
# print(Student_3.Name)
# print(Student_3.ID)
# print(Student_3.Age)
# print(Student_3.Department)
# print(Student_3.Course)
# print(Student_3.Term)
#
# #Method_2
# def display(self):
#     print('Name of the student:' self.Name)
#     print('Student age:' self.Age)
#     print('Student ID': self.ID)
#     print('Student age': self.Age)
#     print('Student department': self.Department)
#     print('Student course': self.Course)
#     print('Student term': self.Term)
#
# Student_1('Bryan', 202020, 20, 'SETAS', 'Comp100', 'Winter')
# Student_2('Alex', 303030, 21, 'Business', 'Accounts', 'Summer')
# Student_3('Bob', 101010, 26, 'Arts', 'History', 'Fall')
# Student_1.display()
# print()
# Student_2.display()
# Student_3.display()


# ===== IMPROVED VERSION =====
# Create first student object
Student_1 = Student('Bryan', 202020, 20, 'SETAS', 'Comp100', 'Winter')
# Display Student_1 information
Student_1.display()
# Add blank line for spacing
print()

# Create second student object
Student_2 = Student('Alex', 303030, 21, 'Business', 'Accounts', 'Summer')
# Display Student_2 information
Student_2.display()
# Add blank line for spacing
print()

# Create third student object
Student_3 = Student('Bob', 101010, 26, 'Arts', 'History', 'Fall')
# Display Student_3 information
Student_3.display()
# Add blank line for spacing
print()

