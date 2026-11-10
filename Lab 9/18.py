import sqlite3

con = sqlite3.connect("employee.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS employees(
    eid INTEGER PRIMARY KEY,
    name TEXT,
    designation TEXT,
    dept TEXT,
    salary REAL
)
""")
 
cur.execute("SELECT COUNT(*) FROM employees")
if cur.fetchone()[0] == 0:
    data = [
        (101, "Aman", "Developer", "CSE", 50000),
        (102, "Riya", "Analyst", "CSE", 60000),
        (103, "Raj", "Engineer", "ECE", 45000),
        (104, "Neha", "Manager", "ECE", 70000)
    ]

    cur.executemany(
        "INSERT INTO employees VALUES (?, ?, ?, ?, ?)", data
    )
    con.commit()

dept = input("Enter department: ")

cur.execute(
    "SELECT eid, name, designation, salary FROM employees WHERE dept=?",
    (dept,)
)

rows = cur.fetchall()

print("\nSalary Report for", dept)

if rows:
    total = 0

    for row in rows:
        print(row)
        total += row[3]

    print("Number of employees:", len(rows))
    print("Total salary:", total)
    print("Average salary:", total / len(rows))
else:
    print("No employees found.")

con.close()