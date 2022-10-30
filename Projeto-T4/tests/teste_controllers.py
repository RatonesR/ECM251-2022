from src.controllers.user_controller import UserController
from src.models.user import User

controller = UserController()
nome_teste = input("digite seu nome: ")
email_teste = input("digite seu email: ")
senha_teste = input("digite sua senha: ")
new_user = controller.cadastrar(nome_teste, email_teste, senha_teste)