class LibraryItem:
    def __init__(self, id, title):
        self.id = id
        self.title = title
        self.issued = False

    def display(self):
        print(self.id, self.title)

    def issue(self):
        if not self.issued:
            self.issued = True
            print(self.title, "issued successfully.")
        else:
            print(self.title, "is already issued.")

    def return_item(self):
        if self.issued:
            self.issued = False
            print(self.title, "returned successfully.")
        else:
            print(self.title, "was not issued.")


class Book(LibraryItem):
    def display(self): print("Book:", self.id, self.title)

class Magazine(LibraryItem):
    def display(self): print("Magazine:", self.id, self.title)

class Journal(LibraryItem):
    def display(self): print("Journal:", self.id, self.title)

# Create library items
items = [
    Book(101, "Python Programming"),
    Magazine(102, "Science Today"),
    Journal(103, "Computer Science Research"),
    Book(104, "Data Structures and Algorithms"),
    Journal(105, "Artificial Intelligence Journal"),
    Book(106, "Machine Learning Basics")
]

while True:
    print("\n----- Library Management System -----")
    print("1. Display Items")
    print("2. Issue Item")
    print("3. Return Item")
    print("4. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        print("\nLibrary Items:")
        for item in items:  item.display()

    elif ch == 2:
        id = int(input("Enter Item ID: "))
        found = False

        for item in items:
            if item.id == id:
                item.issue()
                found = True
                break

        if not found: print("Item not found.")

    elif ch == 3:
        id = int(input("Enter Item ID: "))
        found = False
        for item in items:
            if item.id == id:
                item.return_item()
                found = True
                break

        if not found: print("Item not found.")

    elif ch == 4:
        print("Program ended.")
        break

    else: print("Invalid choice.")