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

class TestMagazine(unittest.TestCase):
    def setUp(self):
        clear_database()

    def test_magazine_creation(self):
        magazine = Magazine(1, 'Tech Monthly', 'Technology')
        self.assertEqual(magazine.name, 'Tech Monthly')
        self.assertEqual(magazine.category, 'Technology')

    def test_magazine_articles(self):
        author = Author(1, 'John Doe')
        magazine = Magazine(1, 'Tech Monthly', 'Technology')
        Article(author, magazine, 'The Rise of AI')
        articles = magazine.articles()
        self.assertEqual(len(articles), 1)

    def test_magazine_contributors(self):
        author1 = Author(1, 'John Doe')
        author2 = Author(2, 'Jane Smith')
        magazine = Magazine(1, 'Tech Monthly', 'Technology')
        Article(author1, magazine, 'The Rise of AI')
        Article(author2, magazine, 'Genetic Engineering')
        contributors = magazine.contributors()
        self.assertEqual(len(contributors), 2)

    def test_magazine_article_titles(self):
        author = Author(1, 'John Doe')
        magazine = Magazine(1, 'Tech Monthly', 'Technology')
        Article(author, magazine, 'The Rise of AI')
        titles = magazine.article_titles()
        self.assertEqual(titles, ['The Rise of AI'])

    def test_magazine_contributing_authors(self):
        author1 = Author(1, 'John Doe')
        author2 = Author(2, 'Jane Smith')
        magazine = Magazine(1, 'Tech Monthly', 'Technology')
        Article(author1, magazine, 'The Rise of AI')
        Article(author1, magazine, 'AI in Healthcare')
        Article(author1, magazine, 'AI in Education')
        Article(author2, magazine, 'Genetic Engineering')
        contributing_authors = magazine.contributing_authors()
        self.assertEqual(len(contributing_authors), 1)
        self.assertEqual(contributing_authors[0][1], 'John Doe')

if __name__ == '__main__':
    unittest.main()
