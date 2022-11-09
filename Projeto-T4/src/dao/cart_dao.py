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

    def ver_carrinho(self, id):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Cart INNER JOIN Products, User ON Cart.user_id = User.id AND Cart.prod_id = Products.id WHERE Cart.user_id = {id}
        """)
        resultados = self.cursor.fetchall()
        return resultados
        # resultados = []
        # for resultado in self.cursor.fetchall():
        #     resultados.append(Products(id=resultado[0], name=resultado[1], price=resultado[2], description=resultado[3]))
        # self.cursor.close()
        # return resultados

    def pegar_id_prod(self, name):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT id FROM Products
            WHERE name = '{name}'
        """)
        id = self.cursor.fetchone()[0]
        self.cursor.close()
        return id

    def add_item_carrinho(self, cart):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            INSERT INTO Cart (prod_id, user_id)
            VALUES(?,?);
        """, (cart.prod_id, cart.user_id))
        self.conn.commit()
        self.cursor.close()

    def del_item_carrinho(self, prod_id, user_id):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            DELETE FROM Cart 
            WHERE prod_id = '{prod_id}' AND user_id = '{user_id}'
        """)
        self.conn.commit()
        self.cursor.close()

    # def ver_produtos(self):
    #     self.cursor = self.conn.cursor()
    #     self.cursor.execute("""
    #         SELECT * FROM Products;
    #     """)
    #     resultados = []
    #     for resultado in self.cursor.fetchall():
    #         resultados.append(Products(id=resultado[0], name=resultado[1], price=resultado[2], description=resultado[3]))
    #     self.cursor.close()
    #     return resultados