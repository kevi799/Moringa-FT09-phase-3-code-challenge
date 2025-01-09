import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
   def test_author_creation(self):
    author = Author("John Doe", 1)
    self.assertEqual(author.name, "John Doe")
    self.assertEqual(author.id, 1)


    def test_article_creation(self):
        article = Article("Test Title", "Test Content", 1, 1,1)
        self.assertEqual(article.title, "Test Title")

    def test_magazine_creation(self):
        magazine = Magazine( "Tech Weekly",1)
        self.assertEqual(magazine.name, "Tech Weekly")

if __name__ == "__main__":
    unittest.main()
