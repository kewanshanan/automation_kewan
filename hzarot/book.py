class Book:
    def __init__(self, title, author, year, genre):
        self._title = title
        self._author = author
        self._year = year
        self._genre = genre

    def __str__(self):
        return f"{self._title} by {self._author}, {self._year}, Genre: {self._genre}"
