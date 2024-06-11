import unittest
import sqlite3
from models.author import Author
from models.magazine import Magazine
from models.article import Article

def clear_database():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM authors')
    cursor.execute('DELETE FROM magazines')
    cursor.execute('DELETE FROM articles')
    connection.commit()
    connection.close()

class TestAuthor(unittest.TestCase):
    def setUp(self):
        clear_database()

    def test_author_creation(self):
        author = Author(1, 'John Doe')
        self.assertEqual(author.name, 'John Doe')

    def test_author_articles(self):
        author = Author(1, 'John Doe')
        magazine = Magazine(1, 'Tech Monthly', 'Technology')
        Article(author, magazine, 'The Rise of AI')
        articles = author.articles()
        self.assertEqual(len(articles), 1)

    def test_author_magazines(self):
        author = Author(1, 'John Doe')
        magazine1 = Magazine(1, 'Tech Monthly', 'Technology')
        magazine2 = Magazine(2, 'Science Daily', 'Science')
        Article(author, magazine1, 'The Rise of AI')
        Article(author, magazine2, 'Genetic Engineering')
        magazines = author.magazines()
        self.assertEqual(len(magazines), 2)

if __name__ == '__main__':
    unittest.main()
