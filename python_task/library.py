import json
import datetime
from book import Book  # Assuming Book class is defined in book.py

class Library:
    def __init__(self, json_path='library.json'):
        self.json_path = json_path
        self.books = self.load_library()

    def read_json(self):
        try:
            with open(self.json_path, 'r') as f:
                data = json.load(f)
                # Ensure that 'books' key exists in the JSON data
                return data.get("books", [])
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def load_library(self):
        books_data = self.read_json()
        # Ensure that the data is a list of dictionaries
        if isinstance(books_data, list):
            return [Book(**book) for book in books_data]
        else:
            return []

    def save_library(self):
        with open(self.json_path, 'w') as f:
            json.dump({"books": [book.__dict__ for book in self.books]}, f, default=str, indent=4)

    def add_book(self, book):
        if not self.book_exists(book.title, book.author, book.publication_year, book.genre):
            self.books.append(book)
            self.save_library()
            print("Book added successfully.")
            self.print_library()
        else:
            print(f"Book '{book.title}' by '{book.author}' and '{book.publication_year}' and '{book.genre}' "
                  f"already exists in the library. Cannot add.")

    def edit_book(self, index, title=None, author=None, publication_year=None, genre=None):
        if 0 <= index < len(self.books):
            self.books[index].title = title or self.books[index].title
            self.books[index].author = author or self.books[index].author
            self.books[index].publication_year = publication_year or self.books[index].publication_year
            self.books[index].genre = genre or self.books[index].genre
            self.books[index].last_updated = datetime.datetime.now().replace(microsecond=0)
            self.save_library()
            print("Book edited successfully.")
            self.print_library()
        else:
            print("Invalid book index.")

    def delete_book(self, index):
        if 0 <= index < len(self.books):
            del self.books[index]
            self.save_library()
            print("Book deleted successfully.")
            self.print_library()
        else:
            print("Invalid book index.")

    def print_library(self):
        if self.books:
            print("\nCurrent Library:")
            for i, book in enumerate(self.books):
                print(f"{i}. {book}")
        else:
            print("\nThe library is empty.")

    def list_books(self):
        return self.books

    def book_exists(self, title, author, publication_year, genre):
        for existing_book in self.books:
            if (existing_book.title == title and existing_book.author == author and publication_year == publication_year
                    and genre == genre):
                return True
        return False

    def save_and_exit(self):
        self.save_library()
        print("Library saved. Exiting...")
        self.print_library()

    def filter_books(self, author=None, genre=None):
        filtered_books = self.books
        if author:
            filtered_books = list(filter(lambda book: book.author == author, filtered_books))
        if genre:
            filtered_books = list(filter(lambda book: book.genre == genre, filtered_books))
        return filtered_books

