class Book:
    # constructor method
    def __init__(self, title, author, year):
        self.author  = author
        self.title = title
        self.year = year

    # Represent an object as a sting
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
     
    #String representation of the object
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
    
    # destuctor method
    def __del__(self):
        print(f"Deleting {self.title}")
