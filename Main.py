class Book:
    def __init__(self, title, author, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__available = True

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def genre(self):
        return self.__genre

    @property
    def availability(self):
        return self.__available

    @availability.setter
    def availability(self, is_available):
        self.__available = is_available

    def __str__(self):
        return f"{self.title} by {self.author} - Genre: {self.genre} - {'Available' if self.availability else 'Borrowed'}"

class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

    def borrow_book(self, book):
        if book.availability:
            self.__borrowed_books.append(book.title)
            book.availability = False
            return f"{book.title} has been borrowed."
        else:
            return f"{book.title} is not available."

    def return_book(self, book):
        try:
            self.__borrowed_books.remove(book.title)
            book.availability = True
            return f"{book.title} has been returned."
        except ValueError:
            return f"{book.title} is not borrowed by {self.__name}."

class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    def __str__(self):
        return f"Author: {self.__name}, Bio: {self.__biography}"

def validate_genre(genre):
    valid_genres = ["Science Fiction", "Drama", "Action", "Biography", "History", "Mystery"]
    if genre not in valid_genres:
        raise ValueError(f"Invalid genre. Please choose from {valid_genres}")

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

        if choice == "6":
            break
        # Implement the actions for each choice here

def user_menu():
    while True:
        print("\nUser Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")
        print("4. Return to Main Menu")
        choice = input("Select an option: ")

        if choice == "4":
            break
        # Implement the actions for each choice here

def author_menu():
    while True:
        print("\nAuthor Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")
        print("4. Return to Main Menu")
        choice = input("Select an option: ")

        if choice == "4":
            break
        # Implement the actions for each choice here

if __name__ == "__main__":
    main_menu()
