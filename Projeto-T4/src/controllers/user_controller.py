from src.models.user import User
from src.dao.user_dao import UserDAO

class UserController:
    def __init__(self) -> None:
        pass

    def checklogin(self, name, password) -> User:
        user = UserDAO.get_instance().checklogin(name, password)
        return user

    def cadastrar(self, usuario) -> bool:
        try:
            UserDAO.get_instance().cadastrar(usuario)
        except:
            return False
        return True

    def excluir_conta(self, usuario) -> bool:
        try:
            UserDAO.get_instance().excluir_conta(usuario)
        except:
            return False
        return True