# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as available."""
        self._is_checked_out = False

    def is_available(self):
        """Return True if the book is available for checkout."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """Add a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by its title."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False  # Book not found or already checked out

    def return_book(self, title):
        """Return a book by its title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False  # Book not found or not checked out

    def list_available_books(self):
        """Print all books that are currently available."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
