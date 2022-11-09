from src.dao.cart_dao import CartDAO
from src.models.cart import Cart
from src.models.products import Products
from src.controllers.user_controller import UserController

class CartController:
    def __init__(self) -> None:
        pass

    def total_compra(self) -> float:
        pass

    def pegar_carrinho(self, user_id) -> list[Cart]:
        return CartDAO.get_instance().pegar_carrinho(user_id)

    def ver_carrinho(self, id) -> Products:
        return CartDAO.get_instance().ver_carrinho(id)

    def add_item_carrinho(self, cart) -> bool:
        try:
            CartDAO.get_instance().add_item_carrinho(cart)
        except:
            return False
        return True

    def pegar_id_prod(self, name) -> Products:
        id_prod = CartDAO.get_instance().pegar_id_prod(name)
        return id_prod

    def del_item_carrinho(self, prod_id, user_id) -> bool:
        try:
            CartDAO.get_instance().del_item_carrinho(prod_id, user_id)
        except:
            return False
        return True

    # def ver_produtos(self, prod_id):
    #     CartDAO.get_instance().ver_produtos(prod_id)