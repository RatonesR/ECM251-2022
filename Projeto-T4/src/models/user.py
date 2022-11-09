class User:
    def __init__(self, name, email, password) -> None:
        self.id = None
        self.name = name
        self.email = email
        self.password = password
    
    def validar_user(self):
        return self.validar_campo(self.name) and self.validar_campo(self.email) and self.validar_campo(self.password)
    
    def validar_campo(self, campo):
        return campo != None and campo != ''


    def __str__(self) -> str:
        return f'User["name":{self.name}, "email":{self.email}, "password":{self.password}]]'