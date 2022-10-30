class Cart:
    def __init__(self, id, prod_id, user_id, cart_id) -> None:
        self.id = id
        self.prod_id = prod_id
        self.user_id = user_id
        self.cart_id = cart_id

    def __str__(self) -> str:
        return f'Cart["id":{self.id}, "prod_id":{self.prod_id}, "user_id":{self.user_id}, "cart_id":{self.cart_id}]]'