'''
Develop a Python program to manage student records using lists and dictionaries, supporting insertion, deletion, and search operations.
'''

students = []
 
def insert_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    branch = input("Enter Branch: ")

    student = {
        "Roll No": roll,
        "Name": name,
        "Age": age,
        "Branch": branch
    }

    students.append(student)
    print("Student record inserted successfully.")
 
def delete_student():
    roll = input("Enter Roll No to delete: ")

    found = False

    for student in students:
        if student["Roll No"] == roll:
            students.remove(student)
            found = True
            print("Student record deleted.")
            break

    if not found:
        print("Student not found.")
 
def search_student():
    roll = input("Enter Roll No to search: ")

    found = False

    for student in students:
        if student["Roll No"] == roll:
            print("\nStudent Found")
            print(student)
            found = True
            break

    if not found:
        print("Student not found.")
 
def display_students():
    if len(students) == 0:
        print("No student records available.")
    else:
        print("\nStudent Records:")

        for student in students:
            print(student)
 
while True:
    print("\n----- Student Record Management -----")
    print("1. Insert Student")
    print("2. Delete Student")
    print("3. Search Student")
    print("4. Display All Students")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        insert_student()

    elif choice == 2:
        delete_student()

    elif choice == 3:
        search_student()

    elif choice == 4:
        display_students()

    elif choice == 5:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")
        print("Please enter a valid option (1-5).")
