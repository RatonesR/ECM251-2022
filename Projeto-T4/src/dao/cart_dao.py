import sqlite3
from src.models.cart import Cart
from src.models.products import Products
class CartDAO:
    
    _instance = None

    def __init__(self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = CartDAO()
        return cls._instance

    def _connect(self):
        self.conn = sqlite3.connect('./databases/sqlite.db')

    def pegar_carrinho(self, user_id):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Cart
            WHERE user_id = {user_id}
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(Cart(id=resultado[0], prod_id=resultado[1], user_id=resultado[2], cart_id=resultado[3]))
        self.cursor.close()
        return resultados

    def ver_carrinho(self, id):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
        SELECT * FROM Products
            WHERE id = {id}
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(Cart(id=resultado[0], name=resultado[1], price=resultado[2], description=resultado[3]))
        self.cursor.close()
        return resultados

    def add_item_carrinho(self, cart):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            INSERT INTO User (prod_id, user_id)
            VALUES(?,?);
        """, (cart.prod_id, cart.user_id))
        self.conn.commit()
        self.cursor.close()

    def del_item_carrinho(self, prod_id):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                DELETE FROM Cart 
                WHERE prod_id = '{prod_id}'
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True

    def ver_produtos(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Products;
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(Products(id=resultado[0], name=resultado[1], price=resultado[2], description=resultado[3]))
        self.cursor.close()
        return resultados