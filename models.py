# models.py

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
        if book.title in self.__borrowed_books:
            self.__borrowed_books.remove(book.title)
            book.availability = True
            return f"{book.title} has been returned."
        else:
            return f"{book.title} is not borrowed by {self.__name}."

class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    def __str__(self):
        return f"Author: {self.__name}, Bio: {self.__biography}"
