# operations.py

from models import Book, User, Author

# These lists will serve as in-memory databases
books = []
users = []
authors = []

def add_new_book():
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    genre = input("Enter the book genre: ")
    publication_date = input("Enter the publication date: ")
    new_book = Book(title, author, genre, publication_date)
    books.append(new_book)
    print(f"Book added: {new_book}")

def borrow_a_book():
    title = input("Enter the title of the book to borrow: ")
    for book in books:
        if book.title.lower() == title.lower():
            current_user = input("Enter your library ID: ")
            user = next((u for u in users if u.library_id == current_user), None)
            if user:
                print(user.borrow_book(book))
            else:
                print("User not found.")
            return
    print("Book not found.")

def return_a_book():
    title = input("Enter the title of the book to return: ")
    for book in books:
        if book.title.lower() == title.lower():
            current_user = input("Enter your library ID: ")
            user = next((u for u in users if u.library_id == current_user), None)
            if user:
                print(user.return_book(book))
            else:
                print("User not found.")
            return
    print("Book not found.")

def search_for_a_book():
    title = input("Enter the title of the book to search for: ")
    found_books = [book for book in books if title.lower() in book.title.lower()]
    if found_books:
        for book in found_books:
            print(book)
    else:
        print("No books found.")

def display_all_books():
    if books:
        for book in books:
            print(book)
    else:
        print("No books available.")

def add_new_user():
    name = input("Enter the user's name: ")
    library_id = input("Enter the user's library ID: ")
    new_user = User(name, library_id)
    users.append(new_user)
    print(f"User added: {new_user}")

def view_user_details():
    library_id = input("Enter the user's library ID: ")
    user = next((u for u in users if u.library_id == library_id), None)
    if user:
        print(user)
    else:
        print("User not found.")

def display_all_users():
    if users:
        for user in users:
            print(user)
    else:
        print("No users available.")

def add_new_author():
    name = input("Enter the author's name: ")
    biography = input("Enter the author's biography: ")
    new_author = Author(name, biography)
    authors.append(new_author)
    print(f"Author added: {new_author}")

def view_author_details():
    name = input("Enter the author's name to view details: ")
    author = next((a for a in authors if a.name.lower() == name.lower()), None)
    if author:
        print(author)
    else:
        print("Author not found.")

def display_all_authors():
    if authors:
        for author in authors:
            print(author)
    else:
        print("No authors available.")

def main_menu():
    while True:
        print("\nWelcome to the Library Management System!")
        print("Main Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Quit")
        choice = input("Select an option: ")

        if choice == "1":
            book_menu()
        elif choice == "2":
            user_menu()
        elif choice == "3":
            author_menu()
        elif choice == "4":
            print("Exiting system.")
            break
        else:
            print("Invalid option. Please try again.")

def book_menu():
    while True:
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        print("6. Return to Main Menu")
        choice = input("Select an option: ")

        if choice == "1":
            add_new_book()
        elif choice == "2":
            borrow_a_book()
        elif choice == "3":
            return_a_book()
        elif choice == "4":
            search_for_a_book()
        elif choice == "5":
            display_all_books()
        elif choice == "6":
            break

def user_menu():
    while True:
        print("\nUser Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")
        print("4. Return to Main Menu")
        choice = input("Select an option: ")

        if choice == "1":
            add_new_user()
        elif choice == "2":
            view_user_details()
        elif choice == "3":
            display_all_users()
        elif choice == "4":
            break

def author_menu():
    while True:
        print("\nAuthor Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")
        print("4. Return to Main Menu")
        choice = input("Select an option: ")

        if choice == "1":
            add_new_author()
        elif choice == "2":
            view_author_details()
        elif choice == "3":
            display_all_authors()
        elif choice == "4":
            break
