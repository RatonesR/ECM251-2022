from models.user import User


class UserController():
    def __init__(self) -> None:
        self.users = []
    def checkUser(self,user):
        return user in self.users

    def checkLogin(self, name, password):
        user_teste = User(name=name, password=password)
        for user in self.users:
            if user.name == user_teste.name and user.password == user_teste.password:
                return True
        return False

    def cadastro(self, name, password):
        user_teste2 = User(name=name, password=password)
        self.users.append(user_teste2.name, user_teste2.password)
