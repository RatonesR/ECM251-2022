class Cart:
    def __init__(self, prod_id, user_id) -> None:
        self.id = None
        self.prod_id = prod_id
        self.user_id = user_id

    def __str__(self) -> str:
        return f'Cart["prod_id":{self.prod_id}, "user_id":{self.user_id}]]'