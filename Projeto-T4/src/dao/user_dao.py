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
        self.conn = sqlite3.connect('./databases/sqlite.db', check_same_thread=False)

    def checklogin(self, name, password):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM User
            WHERE name = '{name}' AND password = '{password}';
        """)
        usuario = None
        resultado = self.cursor.fetchone()
        if resultado != None:
            usuario = User(name=resultado[1], email=resultado[2], password=resultado[3])
        self.cursor.close()
        return usuario

    def cadastrar(self, user):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            INSERT INTO User (name, email, password)
            VALUES(?,?,?);
        """, (user.name, user.email, user.password))
        self.conn.commit()
        self.cursor.close()

    def excluir_conta(self, id):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            DELETE FROM User
            WHERE id = '{id}'
        """)
        self.conn.commit()
        self.cursor.close()

    def pegar_id(self, name, password):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT id FROM User
            WHERE name = '{name}' AND password = '{password}';
        """)
        id = self.cursor.fetchone()[0]
        self.cursor.close()
        return id

    def pegar_nome(self, id):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT name FROM User
            WHERE id = '{id}';
        """)
        name = self.cursor.fetchone()[0]
        self.cursor.close()
        return name

    def pegar_email(self, id):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT email FROM User
            WHERE id = '{id}';
        """)
        email = self.cursor.fetchone()[0]
        self.cursor.close()
        return email

    def pegar_senha(self, id):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT password FROM User
            WHERE id = '{id}';
        """)
        password = self.cursor.fetchone()[0]
        self.cursor.close()
        return password

    def editar_perfil(self, name, email, password, id):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            UPDATE User SET
            name = '{name}',
            email = '{email}',
            password = '{password}'
            WHERE id = '{id}'
        """)
        self.conn.commit()
        self.cursor.close()