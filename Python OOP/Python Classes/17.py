# Library Management System
# Design a simple Library Management System using Object-Oriented Programming in Python.
# The system should:
# Allow users to add books to the library.
# Allow users to view all available books.
# Allow users to issue a book, i.e., borrow it from the library if it exists.
class Library:
    def __init__(self):
        self.books=[]
    def add_books(self,book):
        self.books.append(book)
        print(f"Book {book} add in the library ")
    def view_books(self):
        if not self.books:
            print("No books available in the library")
        else:
            print("\n Available Books ")
            for book in self.books:
                print(f"- {book}")
    def issue_books(self,book):
        if book in self.books:
            self.books.remove(book)
            print(f"Issued book {book}")
        else:
            print("Book not available in the library")
library=Library()
while True:
    print("\n Library Menu ")
    print("1. Add Books")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Exit")
    choice=input("Enter your choice: ")
    if choice =='1':
        book_name=input("Enter the book name: ")
        library.add_books(book_name)
    elif choice =='2':
        library.view_books()
    elif choice =='3':
        issue_book=input("Enter the book you want to issue: ")
        library.issue_books(issue_book)
    elif choice =='4':
        print("Exiting Library Menu")
        break
    else:
        print("Invalid Choice Please enter the valid choice Thankyou! ")
