from book_class import Book

# Create a Book instance
book1 = Book("1984", "George Orwell", 1949)

# Print the book instance using __str__
print(book1)

# Print the book instance using __repr__
print(repr(book1))

# Delete the book instance to trigger __del__
del book1

