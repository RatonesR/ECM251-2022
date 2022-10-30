from src.dao.user_dao import UserDAO
from src.dao.cart_dao import CartDAO
from src.models.user import User


#user = User(id = 123, name = "oi", email = "ola", password = "salve")
#cadastro = UserDAO.get_instance().cadastrar(user)

# name = "oi"
# email = "ola"
# password = "salve"
# excluir = UserDAO.get_instance().excluir_conta(name, email, password)

# prod = CartDAO.get_instance().ver_produtos()
# for produto in prod:
#     print(produto)

# prod_id_teste = input("digite o id o produto: ")
# user_id_teste = input("digite seu id: ")
# cart_id_teste = input("digite o id do carrinho: ")

# carrinho = CartDAO.get_instance().ver_carrinho(cart_id_teste)
# if carrinho == []:
#     print("carrinho nao encontrado")
# else:
#     print("carrinho ja existe")
#     add = CartDAO.get_instance().add_item_carrinho(prod_id_teste, user_id_teste, cart_id_teste)