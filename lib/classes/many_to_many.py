class Article:
    
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author class")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine class")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")
        self._title = title
        self._author = author
        self.magazine = magazine
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise ValueError("Author must be an instance of Author class")
        self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine class")
        self._magazine = new_magazine
class Author:

    all = []
    def __init__(self, name):
        if not isinstance(name, str) or not name:
            raise ValueError(
                "Name must be a non-empty string"
            )
        self._name = name
        self._articles = []
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    def articles(self):
        self._articles = [article for article in Article.all if article.author == self]
        return self._articles

    def magazines(self):
        author_articles = self.articles()
        return list(set(article.magazine for article in author_articles))

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise ValueError("magazine must be an instance of Magazine class")
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def topic_areas(self):
        if not self.articles():
            return None
        return list(set(magazine.category for magazine in self.magazines()))

class Magazine:

    all = []
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        if not isinstance(category, str):
            raise ValueError("Category must be a non string")
        self._name = name
        self._category = category
        self._articles = []
        Magazine.all.append(self)

    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if not isinstance(category, str) or not category:
            raise ValueError("Category must be a non empty string ")
        self._category = category

    def articles(self):
        self._articles = [article for article in Article.all if article.magazine == self]
        return self._articles

    def contributors(self):
        magazine_articles = self.articles()
        return list(set(article.author for article in magazine_articles))


    def article_titles(self):
        if not self.articles():
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        magazine_articles = self.articles()
        author_count = {}
        for article in magazine_articles:
            author_name = article.author.name
            author_count[author_name] = author_count.get(author_name, 0) + 1
        cont_authors = [author_name for author_name, article_count in author_count.items() if article_count > 2]
        if not cont_authors:
            return None
        return[author for author in Author.all if author.name in cont_authors]
    
    @classmethod
    def top_publisher(cls):
        magazines_with_articles = [magazine for magazine in cls.all if magazine.articles()]
        if not magazines_with_articles:
            return None
        return max(magazines_with_articles, key=lambda magazine: len(magazine.articles()))