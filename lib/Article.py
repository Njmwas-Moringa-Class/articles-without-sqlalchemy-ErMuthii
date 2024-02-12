class Article:
    _all = []

    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        Article._all.append(self)

    @classmethod
    def all(cls):
        return cls._all

    def author(self):
        return self._author

    def magazine(self):
        return self._magazine

    def title(self):
        return self._title
