Library Management System Documentation
Welcome to the Library Management System! This system is designed to manage books, users, and authors efficiently. Below is a detailed guide on how to interact with the system and utilize its features.
Features

1. Book Management

Add a New Book: Allows you to enter details for a new book and add it to the system.
Borrow a Book: Users can borrow a book if it is available.
Return a Book: Allows users to return books they have borrowed.
Search for a Book: Search the library's collection by various criteria such as title, author, or genre.
Display All Books: Lists all the books in the library.
2. User Management

Add a New User: Register a new user with a unique library ID.
View User Details: Display details of a specific user, including borrowed books.
Display All Users: List all users registered in the system.
3. Author Management

Add a New Author: Add authors along with their biographies to the system.
View Author Details: View detailed biographies and list of books by the author.
Display All Authors: Show all authors whose books are available in the library.
Classes and Methods

Class: Book

Attributes:
title: Title of the book.
author: Author of the book.
genre: Genre of the book.
publication_date: Publication date of the book.
availability: Current availability status of the book.
Methods:
__init__: Initializes a new book instance.
__str__: Returns a string representation of the book.
Class: User

Attributes:
name: Name of the user.
library_id: Unique identifier for the user.
borrowed_books: List of books currently borrowed by the user.
Methods:
__init__: Initializes a new user instance.
borrow_book: Allows a user to borrow a book.
return_book: Allows a user to return a borrowed book.
Class: Author

Attributes:
name: Name of the author.
biography: A short biography of the author.
Methods:
__init__: Initializes a new author instance.
__str__: Returns a string representation of the author.


The system includes validation for genres. When adding a new book, the genre must be one of the predefined valid genres: "Science Fiction", "Drama", "Action", "Biography", "History", "Mystery". If an invalid genre is entered, the system will raise a ValueError.
Conclusion

This Library Management System is designed to be user-friendly and efficient in managing a library's operations. Whether you are managing books, users, or authors, this system provides a comprehensive set of tools to help maintain and organize library resources effectively.
