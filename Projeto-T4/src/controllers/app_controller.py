from src.controllers.user_controller import UserController
from src.controllers.cart_controller import CartController
from src.models.user import User
from src.models.cart import Cart
from src .models.products import Products
import uuid

class Application:
    def __init__(self):
        self.user_controller = UserController()
        self.cart_controller = CartController()

    def logar():
        pass

    def cadastrar():
        pass

    def sair():
        pass

    def excluir_conta():
        pass

    def listar_produtos():
        pass

    def add_item_carrinho():
        pass

    def rem_item_carrinho():
        pass

    def limpar_carrinho():
        pass