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
        self.carrinho = None
        self.estado_login = False

    def login2(self, name, email, password):
        self.usuario_logado = User(
            id=None,
            name=name,
            email=email,
            password=password
        )

    def login(self, name, password):
        return self.user_controller.checklogin(name, password)

    # def pegar_user(self):
    #     login = self.user_controller.checklogin()
    #     return 