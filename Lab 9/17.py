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

while True:
    print("\n1. Insert")
    print("2. Display")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        eid = int(input("Employee ID: "))
        name = input("Name: ")
        des = input("Designation: ")
        dept = input("Department: ")
        sal = float(input("Salary: "))

        cur.execute(
            "INSERT INTO employees VALUES (?, ?, ?, ?, ?)",
            (eid, name, des, dept, sal)
        )
        con.commit()
        print("Employee inserted.")

    elif ch == 2:
        cur.execute("SELECT * FROM employees")
        for row in cur.fetchall():
            print(row)

    elif ch == 3:
        eid = int(input("Enter ID to update: "))
        sal = float(input("Enter new salary: "))

        cur.execute(
            "UPDATE employees SET salary=? WHERE eid=?",
            (sal, eid)
        )
        con.commit()
        print("Employee updated." if cur.rowcount else "Employee not found.")

    elif ch == 4:
        eid = int(input("Enter ID to delete: "))

        cur.execute("DELETE FROM employees WHERE eid=?", (eid,))
        con.commit()
        print("Employee deleted." if cur.rowcount else "Employee not found.")

    elif ch == 5:
        break 
    
    else:
        print("Invalid choice.")

con.close()