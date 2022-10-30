class Products:
    def __init__(self, id, name, price, description) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.description = description
    def __str__(self) -> str:
        return f'Products["id":{self.id}, "name":{self.name}, "preco":{self.price}, "description":{self.description}]'