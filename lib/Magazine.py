from Article import Article


class Magazine:
    _all = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
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
      
        return list(set([article.author() for article in Article.all() if article.magazine() == self]))

    def contributing_authors(self):
        authors = {}
        
        for article in Article.all():
            if article.magazine() == self:
                author = article.author()
                if author in authors:
                    authors[author] += 1
                else:
                    authors[author] = 1
        return [author for author, count in authors.items() if count > 2]
