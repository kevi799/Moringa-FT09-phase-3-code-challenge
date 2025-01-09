from database.connection import get_db_connection
from models.author import Author
from models.magazine import Magazine

class Article:
    def __init__(self, title, content, author, magazine, id=None):
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")
        if not isinstance(content, str):
            raise TypeError("Content must be a string.")
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of the Author class.")
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be an instance of the Magazine class.")
        
        self._id = id
        self._title = title
        self._content = content
        self._author_id = author.id
        self._magazine_id = magazine.id

        if id is None:
            self.save_to_db()

    def save_to_db(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
            (self._title, self._content, self._author_id, self._magazine_id)
        )
        conn.commit()
        self._id = cursor.lastrowid
        conn.close()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError("ID must be an integer.")
        self._id = value

    @property
    def title(self):
        return self._title

    @property
    def content(self):
        return self._content

    @property
    def author_id(self):
        return self._author_id

    @property
    def magazine_id(self):
        return self._magazine_id

    def __repr__(self):
        return f"<Article {self.title}>"
