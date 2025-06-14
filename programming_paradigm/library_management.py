# This module defines a simple library management system with Book and Library classes.
# The Library class allows adding books, listing available books, checking out, and returning books.


class Book:
    def __init__(self, title, author):
        # Initialize a Book with title, author, and checked-out status
        self.title = title
        self.author = author
        self._is_checked_out = False  # Initialize the Library with an empty list of books


class Library:
    def __init__(self):
        # Initialize the Library with an empty list of books
        self._books = []


    def add_book(self, title, author):
        # Create a new Book and add it to the library
        try:
            books = Book(title, author)
            self._books.append(books)

            print("Book added successfully")
        except Exception as e:
            print(f"Error: {e}")



    def list_available_books(self):
        """
        List all available (not checked out) books in the library.
        """
        try:
            for book in self._books:
                if book._is_checked_out == False: # Only show books that are not checked out
                    print(f"{book.title} by {book.author}")
        except Exception as e:
            print(f"Error: {e}") 

            
    def check_out_book(self, title):
        """
        Check out a book by title if it is available.
        """
        try:
            # Iterate through the books to find the one with the given title
            for book in self._books:

                if book.title == title and book._is_checked_out == False:
                    book._is_checked_out = True

                    return f"{title} is checked out"
            
            return "Not Available"
        except Exception as e:
            return f"Error: {e}"    
    def return_book(self, title):
        """
        Return a checked out book by title.
        """
        try:
            for book in self._books:

                if book.title == title and book._is_checked_out == True:
                    book._is_checked_out = False

                    return f"{title} Returned"
                
            return f"{title} Not Returned"
        except Exception as e:
            return f"Error: {e}"