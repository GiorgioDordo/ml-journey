import json

class Library:
  def __init__(self, booksList):
    self.booksList = booksList

  def display_books(self):
    print("Books available in the library:")
    for book in self.booksList:
      print(book.title)

  def add_book(self, book):
    self.booksList.append(book)
    print(f"'{book.title}' has been added to the library.")
  
  def remove_book(self, book):
    if book in self.booksList:
      self.booksList.remove(book)
      print(f"'{book.title}' has been removed from the library.")
    else:
      print(f"'{book.title}' is not found in the library.")

  def search_book(self, book):
    if book in self.booksList:
      print(f"'{book.title}' is available in the library.")
    else:
      print(f"'{book.title}' is not available in the library.")

  def save_data(self, book, filename='library_data.json'):
    data = {
      "books": [
        {
          "title": book.title,
          "author": book.author,
          "isbn": book.isbn
        }
        for book in self.booksList
      ]
    }
    with open(filename, 'w') as file:
      json.dump(data, file, indent=4)
    print(f"Library data has been saved to '{filename}'.")
  

class Book:
  def __init__(self, title, author, isbn):
    self.title = title
    self.author = author
    self.isbn = isbn

  def display_info(self):
    print(f"Title: {self.title}")
    print(f"Author: {self.author}")

  def is_available(self, library):
    if self in library.booksList:
      print(f"'{self.title}' is available in the library.")
    else:
      print(f"'{self.title}' is not available in the library.")


book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0061120084")
library = Library([])
library.add_book(book1)
library.save_data(book1)
# library.remove_book(book1)
# library.display_books()
# library.search_book(book1)