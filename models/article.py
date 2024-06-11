import sqlite3

class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        self._create_in_db()

    def _create_in_db(self):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)', 
                       (self.title, self.author.id, self.magazine.id))
        connection.commit()
        connection.close()

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str) and 5 <= len(value) <= 50:
            self._title = value
        else:
            raise ValueError("Title must be a string between 5 and 50 characters")

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine
