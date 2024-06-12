import sqlite3

class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self._create_in_db()

    def _create_in_db(self):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        try:
            cursor.execute('INSERT INTO authors (id, name) VALUES (?, ?)', (self.id, self.name))
        except sqlite3.IntegrityError:
            pass  
        connection.commit()
        connection.close()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")

    def articles(self):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM articles WHERE author_id = ?', (self.id,))
        articles = cursor.fetchall()
        connection.close()
        return articles

    def magazines(self):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute('''
        SELECT DISTINCT magazines.* FROM magazines
        JOIN articles ON magazines.id = articles.magazine_id
        WHERE articles.author_id = ?
        ''', (self.id,))
        magazines = cursor.fetchall()
        connection.close()
        return magazines

    def save(self):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        try:
            cursor.execute('INSERT INTO authors (name) VALUES (?)', (self.name,))
        except sqlite3.IntegrityError:
            pass  
        connection.commit()
        connection.close()

    @staticmethod
    def get_all():
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM authors')
        authors = cursor.fetchall()
        connection.close()
        return authors
