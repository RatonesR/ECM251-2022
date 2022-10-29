import sqlite3
from src.models.user import User

class UserDAO:

    _instance = None

    def __init__(self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = UserDAO()
        return cls._instance

    def _connect(self):
        self.conn = sqlite3.connect('./databases/sqlite.db')

    def cadastrar(self, user):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            INSERT INTO User(name, email, password)
            VALUES(?, ?, ?);
        """,  (user.name, user.email, user.password))
        self.conn.commit()
        self.cursor.close()

    def pegarlogin(self, name, password):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM User
            WHERE name = '{name}' AND password = '{password}';
        """)
        usuario = None
        resultado = self.cursor.fetchone()
        if resultado != None:
            usuario = User(id=resultado[0], name=resultado[1], email=resultado[2], password=resultado[3])
        self.cursor.close()
        return usuario