from models.product import Product

class ProductController():
    def __init__(self) -> None:
        #Carrega os dados dos usuários
        self.products = [
            Product(name="joao", price="arroz"),
        ]