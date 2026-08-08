'''
Develop a Python program to analyse student course enrolments by using set operations (union, intersection, difference) to identify students enrolled in common and unique courses, and tuples to store student details.
'''

students = []
course_sets = []
 
def input_students():
    n = int(input("Enter number of students: "))

    for i in range(n):
        print(f"\nEnter details of Student {i + 1}")

        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
 
        students.append((roll, name))

        m = int(input("Enter number of courses: "))
        courses = set()

        for j in range(m):
            course = input(f"Enter course {j + 1}: ")
            courses.add(course)

        course_sets.append(courses)
 
def display_students():
    print("\nStudent Details")

    for i in range(len(students)):
        print(f"\nStudent {i + 1}: {students[i]}")
        print("Courses:", course_sets[i])
 
def find_union():
    all_courses = set()

    for courses in course_sets:
        all_courses = all_courses.union(courses)

    print(f"\nAll Courses (Union): {all_courses}")
 
def find_common():
    common = course_sets[0]

    for i in range(1, len(course_sets)):
        common = common.intersection(course_sets[i])

    if common:
        print(f"\nCommon Courses among all students: {common}")
    else:
        print("\nNo common courses among all students.")
 
    print("\nPairwise Common Courses:") 
    for i in range(len(students)):
        for j in range(i + 1, len(students)):
            common_pair = course_sets[i].intersection(course_sets[j])

            if common_pair:
                print(f"{students[i][1]} and {students[j][1]}: {common_pair}")
            else:
                print(f"{students[i][1]} and {students[j][1]}: No common courses")
 
def find_unique():
    print("\nUnique Courses:")

    for i in range(len(students)):
        unique = course_sets[i]

        for j in range(len(students)):
            if i != j:
                unique = unique.difference(course_sets[j])

        if unique:
            print(f"{students[i][1]}: {unique}")
        else:
            print(f"{students[i][1]}: No unique courses") 
 
input_students()
display_students()
find_union()
find_common()
find_unique()
