from database.connection import get_db_connection

class Magazine:
    def __init__(self, name, category, id=None):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")

        self._id = id
        self._name = name
        self._category = category

        if id is None:
            self.save_to_db()

    def save_to_db(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO magazines (name, category) VALUES (?, ?)',
            (self._name, self._category)
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
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        self._name = value
        self.update_field_in_db('name', value)

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = value
        self.update_field_in_db('category', value)

    def update_field_in_db(self, field, value):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(f'UPDATE magazines SET {field} = ? WHERE id = ?', (value, self._id))
        conn.commit()
        conn.close()

    def __repr__(self):
        return f"<Magazine {self.name}>"
