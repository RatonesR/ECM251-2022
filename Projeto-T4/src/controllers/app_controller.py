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

    def listar_produtos(self):
        self.cart_controller.ver_produtos()

    def ver_carrinho(self, id_atual):
        retorno = {
            "ITENS":[]
        }
        ver_carrinho = self.cart_controller.ver_carrinho(id_atual)
        for resultado in ver_carrinho:
            retorno["ITENS"].append({"nome": resultado[4], "preço": resultado[5]})
        return retorno

    def total_compra():
        pass

    def add_item_carrinho():
        pass

    def rem_item_carrinho():
        pass

    def limpar_carrinho():
        pass