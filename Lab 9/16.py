import sqlite3

con = sqlite3.connect("student.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students(
    roll INTEGER PRIMARY KEY,
    name TEXT,
    dept TEXT,
    cgpa REAL
)
""")

n = int(input("Enter number of students: "))

for i in range(n):
    roll = int(input("Enter roll number: "))
    name = input("Enter name: ")
    dept = input("Enter department: ")
    cgpa = float(input("Enter CGPA: "))

    cur.execute(
        "INSERT INTO students VALUES (?, ?, ?, ?)",
        (roll, name, dept, cgpa)
    )

con.commit()

cur.execute("SELECT * FROM students")
rows = cur.fetchall()

print("\nStudent Records:")
for row in rows:
    print(row)

con.close()