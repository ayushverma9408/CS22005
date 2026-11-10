import sqlite3
import tkinter as tk
from tkinter import messagebox

con = sqlite3.connect("library.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS books(
    bid INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    status TEXT DEFAULT 'Available'
)
""")
con.commit()


def add_book():
    try:
        bid = int(e1.get())
        title = e2.get()
        author = e3.get()

        if not title or not author:
            messagebox.showerror("Error", "Enter all details")
            return

        cur.execute(
            "INSERT INTO books(bid, title, author) VALUES (?, ?, ?)",
            (bid, title, author)
        )
        con.commit()
        messagebox.showinfo("Success", "Book added")
    except ValueError:
        messagebox.showerror("Error", "Book ID must be an integer")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Book ID already exists")


def issue_book():
    cur.execute(
        "UPDATE books SET status='Issued' WHERE bid=? AND status='Available'",
        (e1.get(),)
    )
    con.commit()

    if cur.rowcount:
        messagebox.showinfo("Success", "Book issued")
    else:
        messagebox.showinfo("Notice", "Book unavailable or ID not found")


def return_book():
    cur.execute(
        "UPDATE books SET status='Available' WHERE bid=? AND status='Issued'",
        (e1.get(),)
    )
    con.commit()

    if cur.rowcount:
        messagebox.showinfo("Success", "Book returned")
    else:
        messagebox.showinfo("Notice", "Issued book not found")


def search_book():
    cur.execute("SELECT * FROM books WHERE bid=?", (e1.get(),))
    row = cur.fetchone()

    if row:
        messagebox.showinfo("Book Details", str(row))
    else:
        messagebox.showinfo("Search", "Book not found")


def show_books():
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()

    output.delete("1.0", tk.END)

    for row in rows:
        output.insert(tk.END, str(row) + "\n")


root = tk.Tk()
root.title("Library Management System")
root.geometry("450x450")

tk.Label(root, text="Library Management System",
         font=("Arial", 16)).pack(pady=10)

tk.Label(root, text="Book ID").pack()
e1 = tk.Entry(root)
e1.pack()

tk.Label(root, text="Book Title").pack()
e2 = tk.Entry(root)
e2.pack()

tk.Label(root, text="Author").pack()
e3 = tk.Entry(root)
e3.pack()

tk.Button(root, text="Add Book", command=add_book).pack(pady=3)
tk.Button(root, text="Issue Book", command=issue_book).pack(pady=3)
tk.Button(root, text="Return Book", command=return_book).pack(pady=3)
tk.Button(root, text="Search Book", command=search_book).pack(pady=3)
tk.Button(root, text="Show All Books", command=show_books).pack(pady=3)

output = tk.Text(root, height=7, width=50)
output.pack(pady=10)

root.mainloop()
con.close()