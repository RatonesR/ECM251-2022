class Product():
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
    def __str__(self) -> str:
        return f'Product(name"{self.name}, price:{self.price})'