from Article import Article


class Magazine:
    _all = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []  # Initialize the _articles attribute
        Magazine._all.append(self)

    @classmethod
    def all(cls):
        return cls._all

    @classmethod
    def find_by_name(cls, name):
        for magazine in cls._all:
            if magazine.name() == name:
                return magazine

    @classmethod
    def article_titles(cls):
        return [article.title() for magazine in cls._all for article in magazine.articles()]

    def name(self):
        return self._name

    def category(self):
        return self._category

    def contributors(self):
        return list(set([article.author() for article in self.articles()]))

    def add_article(self, article):
        self._articles.append(article)  # Use self._articles to access and modify the list

    def articles(self):
        return self._articles

    def contributing_authors(self):
        authors = {}
        for article in self.articles():  # Iterate over self.articles() instead of Article.all()
            author = article.author()
            if author in authors:
                authors[author] += 1
            else:
                authors[author] = 1
        return [author for author, count in authors.items() if count > 2]
