import sqlite3

class Magazine:
    def __init__(self, id=None, name=None, category=None):
        self.id = id
        self.name = name
        self.category = category
        self._create_in_db()

    def _create_in_db(self):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        try:
            cursor.execute('INSERT INTO magazines (id, name, category) VALUES (?, ?, ?)', (self.id, self.name, self.category))
        except sqlite3.IntegrityError:
            pass  
        connection.commit()
        connection.close()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            raise ValueError("Name must be a string between 2 and 16 characters")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            raise ValueError("Category must be a non-empty string")

    def save(self):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (self.name, self.category))
        connection.commit()
        connection.close()

    def articles(self):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM articles WHERE magazine_id = ?', (self.id,))
        articles = cursor.fetchall()
        connection.close()
        return articles

    def contributors(self):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute('''
            SELECT DISTINCT authors.* FROM authors
            JOIN articles ON authors.id = articles.author_id
            WHERE articles.magazine_id = ?
        ''', (self.id,))
        authors = cursor.fetchall()
        connection.close()
        return authors

    def article_titles(self):
        articles = self.articles()
        return [article[1] for article in articles]

    def contributing_authors(self):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute('''
            SELECT authors.*, COUNT(articles.id) as article_count FROM authors
            JOIN articles ON authors.id = articles.author_id
            WHERE articles.magazine_id = ?
            GROUP BY authors.id
            HAVING article_count > 2
        ''', (self.id,))
        authors = cursor.fetchall()
        connection.close()
        return authors if authors else None

    @staticmethod
    def get_all():
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM magazines')
        magazines = cursor.fetchall()
        connection.close()
        return magazines
