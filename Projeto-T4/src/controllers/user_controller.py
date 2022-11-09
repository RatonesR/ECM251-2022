from src.models.user import User
from src.dao.user_dao import UserDAO

class UserController:
    def __init__(self) -> None:
        pass

    def checklogin(self, name, password) -> User:
        user = UserDAO.get_instance().checklogin(name, password)
        return user

    def cadastrar(self, user) -> bool:
        try:
            UserDAO.get_instance().cadastrar(user)
        except:
            return False
        return True

    def excluir_conta(self, name, email, password) -> bool:
        try:
            UserDAO.get_instance().excluir_conta(name, email, password)
        except:
            return False
        return True

    def pegar_id(self, name, password) -> User:
        id = UserDAO.get_instance().pegar_id(name, password)
        return id

    def editar_perfil(self, name, email, password, id) -> bool:
        try:
            UserDAO.get_instance().editar_perfil(name, email, password, id)
        except:
            return False
        return True