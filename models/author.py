import sqlite3

class Author:
    def __init__(self, id, name):
        self.id = id
        self._name = name
        self._create_in_db()

    def _create_in_db(self):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO authors (id, name) VALUES (?, ?)', (self.id, self._name))
        connection.commit()
        connection.close()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if isinstance(value, int):
            self._id = value
        else:
            raise ValueError("ID must be an integer")

    @property
    def name(self):
        return self._name
