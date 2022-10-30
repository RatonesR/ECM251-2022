from src.dao.cart_dao import CartDAO
from src.models.cart import Cart
from src.controllers.user_controller import UserController

class CartController:
    def __init__(self) -> None:
        pass

    def total_compra(self) -> float:
        pass

    def ver_carrinho(self, cart_id) -> list[Cart]:
        return CartDAO.get_instance().ver_carrinho(cart_id)

    def del_item_carrinho(self, prod_id) -> bool:
        return CartDAO.get_instance().del_item_carrinho(prod_id)

    def add_item_carrinho(self, prod_id) -> None:
        CartDAO.get_instance().add_item_carrinho(prod_id)

    def ver_produtos(self, prod_id):
        CartDAO.get_instance().ver_produtos(prod_id)