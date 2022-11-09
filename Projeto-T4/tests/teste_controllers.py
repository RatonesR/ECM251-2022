from src.controllers.user_controller import UserController
from src.controllers.cart_controller import CartController
from src.models.user import User
from src.models.cart import Cart

uc = UserController()
cc = CartController()
id_user = None

### VERIFICANDO CHECKUSER E PEGAR_ID
print("vamos checar sua conta!")
name = input("digite seu nome:\n")
password = input("digite sua senha:\n")
checar = uc.checklogin(name, password)
if checar == None:
    print("usuario nao encontrado!")
else:
    print("SUCESSO!!!")
    id_user = uc.pegar_id(name, password)

### VERIFICANDO CADASTRAR 
# print("vamos cadastrar sua conta!")
# name_teste = input("digite seu nome:\n")
# email_teste = input("digite seu email:\n")
# password_teste = input("digite sua senha:\n")
# user = User(name = name_teste, email = email_teste, password = password_teste)
# validar = user.validar_user()
# if validar == True:
#     usuario = uc.cadastrar(User(name = name_teste, email = email_teste, password = password_teste))
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
# nome_produto = input("digite o produto desejado:\n")
# id_produto = cc.pegar_id_prod(nome_produto)
# carrinho = cc.add_item_carrinho(Cart(prod_id = id_produto, user_id = id_user))
# if carrinho == False:
#     print("produto não encontrado!")
# else:
#     print("produto adicionado!")

###VERIFICANDO DEL_ITEM_CARRINHO
# nome_produto = input("qual produto deseja remover?\n")
# id_produto = cc.pegar_id_prod(nome_produto)
# carrinho = cc.del_item_carrinho(id_produto, id_user)
# if carrinho == False:
#     print("produto não encontrado!")
# else:
#     print("item removido!")

###VERIFICANDO VER_CARRINHO
# opcao = int(input("deseja ver carrinho?\n1 - sim\n2 - não\n"))
# if opcao == 1:
#     ver_carrinho = cc.ver_carrinho(id_user)
#     for resultado in ver_carrinho:
#         print(f'Nome: {resultado[4]} Preço: {resultado[5]}')
# elif opcao == 2:
#     print("OK :(")
# else:
#     print("opcao invalida!")

###VERIFICANDO VER_PRODUTOS
# opcao = int(input("deseja ver os produtos da loja?\n1 - sim\n2 - não\n"))
# if opcao == 1:
#     for resultado in range(len(cc.ver_produtos())):
#         nome_produto = cc.ver_produtos()[resultado][1]
#         preco_produto = cc.ver_produtos()[resultado][2]
#         descricao_produto = cc.ver_produtos()[resultado][3]
#         print(f"NOME: '{nome_produto}'    DESCRIÇÃO: '{descricao_produto}'\nPREÇO: {preco_produto}")
# elif opcao == 2:
#     print("OK :(")
# else:
#     print("opcao invalida")