from src.controllers.user_controller import UserController
from src.controllers.cart_controller import CartController
from src.dao.cart_dao import CartDAO
from src.models.user import User


controller = UserController()
### VERIFICANDO CHECKUSER
# print("vamos checar sua conta!")
# name = input("digite seu nome:\n")
# password = input("digite sua senha:\n")
# checar = controller.checklogin(name, password)
# if checar == None:
#     print("usuario nao encontrado!")
# else:
#     print("SUCESSO!!!")

### VERIFICANDO CADASTRAR
# print("vamos cadastrar sua conta!")
# name_teste = input("digite seu nome:\n")
# email_teste = input("digite seu email:\n")
# password_teste = input("digite sua senha:\n")
# usuario = User(name = name_teste, email = email_teste, password = password_teste)
# if usuario == True:
#     print("USUARIO CADASTRADO!!!")
# else:
#     print("falha no cadastro!")

### VERIFICANDO EXCLUIR_CONTA
# print("vamos excluir sua conta!")
# name = input("digite seu nome:\n")
# email = input("digite seu email:\n")
# password = input("digite sua senha:\n")
# excluir = controller.excluir_conta(name, email, password)
# if excluir == True:
#     print("CONTA EXCLUIDA!!!")
# else:
#     print("usuario nao encontrado!")