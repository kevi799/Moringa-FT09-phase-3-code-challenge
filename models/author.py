from database.connection import get_db_connection

class Author:
    def __init__(self, name, id=None):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if len(name.strip()) == 0:
            raise ValueError("Name must be longer than 0 characters.")

        self._id = id
        self._name = name

        if id is None:
            self.save_to_db()

    def save_to_db(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO authors (name) VALUES (?)', (self._name,))
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
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            raise AttributeError("Name cannot be changed after the author is instantiated.")
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        if len(value.strip()) == 0:
            raise ValueError("Name must be longer than 0 characters.")
        self._name = value

    def __repr__(self):
        return f"<Author {self.name}>"
