from src.controllers.user_controller import UserController
from src.controllers.cart_controller import CartController
from src.models.user import User


uc = UserController()
cc = CartController()
id_user = None
### VERIFICANDO CHECKUSER E PEGAR_ID
# print("vamos checar sua conta!")
# name = input("digite seu nome:\n")
# password = input("digite sua senha:\n")
# checar = uc.checklogin(name, password)
# if checar == None:
#     print("usuario nao encontrado!")
# else:
#     print("SUCESSO!!!")
#     id_user = uc.pegar_id(name, password)
#     print(id_user)

### VERIFICANDO CADASTRARa  
# print("vamos cadastrar sua conta!")
# name_teste = input("digite seu nome:\n")
# email_teste = input("digite seu email:\n")
# password_teste = input("digite sua senha:\n")
# usuario = uc.cadastrar(User(name = name_teste, email = email_teste, password = password_teste))
# if usuario == True:
#     print("USUARIO CADASTRADO!!!")
# else:
#     print("falha no cadastro!")

### VERIFICANDO EXCLUIR_CONTA
# print("vamos excluir sua conta!")
# name = input("digite seu nome:\n")
# email = input("digite seu email:\n")
# password = input("digite sua senha:\n")
# excluir = uc.excluir_conta(name, email, password)
# if excluir == True:
#     print("CONTA EXCLUIDA!!!")
# else:
#     print("usuario nao encontrado!")

###VERIFICANDO PEGAR_ID_PROD E ADD_ITEM_CARRINHO
nome_produto = input("digite o produto desejado:\n")
id_produto = cc.pegar_id_prod(nome_produto)
print(id_produto)
