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

class TestArticle(unittest.TestCase):
    def setUp(self):
        clear_database()

    def test_article_creation(self):
        author = Author(1, 'John Doe')
        magazine = Magazine(1, 'Tech Monthly', 'Technology')
        article = Article(author, magazine, 'The Rise of AI')
        self.assertEqual(article.title, 'The Rise of AI')
        self.assertEqual(article.author.name, 'John Doe')
        self.assertEqual(article.magazine.name, 'Tech Monthly')

if __name__ == '__main__':
    unittest.main()
