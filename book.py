import csv

books = {}

def MainProgram():
    while True:
        print("\n=========== Menu ===========")
        print("1. Add a new book")
        print("2. Update a book")
        print("3. Delete a book")
        print("4. Search for a book by title")
        print("5. Display all books")
        print("6. Exit")
        print("============================")
        choice = input("Enter your choice: ")

        if choice == "1":
            AddBook()
        elif choice == "2":
            UpdateBook()
        elif choice == "3":
            DeleteBook()
        elif choice == "4":
            SearchBookByTitle()
        elif choice == "5":
            DisplayBooks()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

def AddBook():
    title = input("Enter the book title: ").lower().strip()
    author = input("Enter the book author: ").lower().strip()

    if title in books and author in books.values():
        print("This book already exists.")
        return
    
    books[title] = author
    print(f"The book '{title.title()}' was added successfully.")
    ExportToCSV()

def UpdateBook():
    title = input("Enter the title of the book to update: ").lower().strip()
    if title not in books:
        print("This book does not exist.")
        return
    
    print("\n1. Update the title")
    print("2. Update the author\n")
    choice = input("Enter your choice: ")
    if choice == "1":
        newTitle = input("Enter the new title: ").lower().strip()
        author = books[title]
        del books[title]
        books[newTitle] = author
    elif choice == "2":
        newAuthor = input("Enter the new author: ").lower().strip()
        books[title] = newAuthor
    
    print(f"The book '{title.title()}' was updated successfully.")
    ExportToCSV()

def DeleteBook():
    title = input("Enter the title of the book to delete: ").lower().strip()
    if title not in books:
        print("This book does not exist.")
        return
    del books[title]
    print(f"The book '{title.title()}' was deleted successfully.")
    ExportToCSV()

def SearchBookByTitle():
    title = input("Enter the book title: ").lower().strip()
    if title not in books:
        print("This book does not exist.")
        return
    author = books[title]
    print("====== Book Information ======")
    print(f"  Title: {title.title()}")
    print(f"  Author: {author.title()}")
    print("===============================")

def DisplayBooks():
    for title, author in books.items():
        print(f"Title: {title.title()}")
        print(f"Author: {author.title()}\n")

def ExportToCSV():
    with open('books.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Author"])

        for title, author in books.items():
            writer.writerow([title, author])
        
        print("Data exported successfully.")

def LoadData():
    try:
        with open('books.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                title, author = row
                books[title] = author
            print("Books loaded successfully.")
    except FileNotFoundError:
        print("No data file found. Starting with an empty catalog.")

LoadData()
MainProgram()
