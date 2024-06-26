import datetime


class Book:
    def __init__(self, title, author, publication_year, genre, last_updated=None):
        self._title = title
        self._author = author
        self._publication_year = publication_year
        self._genre = genre
        self._last_updated = last_updated or datetime.datetime.now().replace(microsecond=0)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
        self._last_updated = datetime.datetime.now().replace(microsecond=0)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value
        self._last_updated = datetime.datetime.now().replace(microsecond=0)

    @property
    def publication_year(self):
        return self._publication_year

    @publication_year.setter
    def publication_year(self, value):
        self._publication_year = value
        self._last_updated = datetime.datetime.now().replace(microsecond=0)

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value):
        self._genre = value
        self._last_updated = datetime.datetime.now().replace(microsecond=0)

    @property
    def last_updated(self):
        return self._last_updated

    @last_updated.setter
    def last_updated(self, value):
        self._last_updated = datetime.datetime.now().replace(microsecond=0)
        value = self._last_updated.replace(microsecond=0)

    def __str__(self):
        return f"{self._title} by {self._author}, {self._publication_year}, Genre: {self._genre}, Last Updated: {self._last_updated}"
