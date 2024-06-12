# app.py

from database.setup import create_tables
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    
    create_tables()

    author_name = input("Enter author's name: ").strip()
    magazine_name = input("Enter magazine name: ").strip()
    magazine_category = input("Enter magazine category: ").strip()
    article_title = input("Enter article title: ").strip()
    article_content = input("Enter article content: ").strip()

    if not (author_name and magazine_name and magazine_category and article_title and article_content):
        print("All fields are required. Please try again.")
        return

    author = Author(None, name=author_name)  
    magazine = Magazine(name=magazine_name, category=magazine_category)
    article = Article(author=author, magazine=magazine, title=article_title)

    try:
        author.save()
        magazine.save()
        article.save()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return

    print("\nMagazines:")
    for mag in Magazine.get_all():
        print(mag)

    print("\nAuthors:")
    for auth in Author.get_all():
        print(auth)

    print("\nArticles:")
    for art in Article.get_all():
        print(art)

if __name__ == "__main__":
    main()
