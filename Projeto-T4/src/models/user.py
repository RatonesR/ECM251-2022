class User:
    def __init__(self, id, name, email, password) -> None:
        self.id = id
        self.name = name
        self.email = email
        self.password = password
    def __str__(self) -> str:
        return f'Item["id":{self.id}, "name":{self.name}, "email":{self.email}, "password":{self.password}]]'