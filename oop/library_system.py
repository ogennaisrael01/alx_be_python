# The base book class
class Book:
    # Initialize the book attibute 
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

# Ebook class that inherites from the base class 
class EBook(Book):
    def __init__(self,title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"{self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self):
        return f"{self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        # Library with an empty list of books
        self.books = []

    def add_book(self, book):
        # Add books to the library. this include Book, Ebook, and PrintBook
        self.books.append(book)
        
    def list_books(self):
        # List all  available Books In the library
        for item in self.books:
            print (f"{type(item).__name__}: {item}")

