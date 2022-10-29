from unicodedata import name
from src.models.user import User
from src.dao.user_dao import UserDAO

class UserController:
    def __init__(self) -> None:
        pass

def pegarlogin(self, id) -> User:
        user = UserDAO.get_instance().pegarlogin(name)
        return user