from src.controllers.user_controller import UserController
from src.controllers.cart_controller import CartController
from src.models.user import User
from src.models.cart import Cart

uc = UserController()
cc = CartController()
id_user = None

### CHECKUSER E PEGAR_ID
# print("vamos checar sua conta!")
# name = input("digite seu nome:\n")
# password = input("digite sua senha:\n")
# checar = uc.checklogin(name, password)
# if checar == None:
#     print("usuario nao encontrado!")
# else:
#     print("SUCESSO!!!")
#     id_user = uc.pegar_id(name, password)
#     print(checar)

### PEGAR_NOME E PEGAR_EMAIL
# print(f"SEU NOME É: {uc.pegar_nome(id_user)}")
# print(f"SEU EMAIL É: {uc.pegar_email(id_user)}")

### CADASTRAR 
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

### EDITAR_PERFIL
# print("vamos editar seu perfil!")
# new_name = input("digite seu novo username:")
# new_email = input("digite seu novo email:")
# new_password = input("digite sua nova senha:")
# editar = uc.editar_perfil(new_name, new_email, new_password, id_user)
# print("alterações salvas!")

### EXCLUIR_CONTA
# print("vamos excluir sua conta!")
# name = input("digite seu nome:\n")
# email = input("digite seu email:\n")
# password = input("digite sua senha:\n")
# excluir = uc.excluir_conta(name, email, password)
# if excluir == True:
#     print("CONTA EXCLUIDA!!!")
# else:
#     print("usuario nao encontrado!")

### PEGAR_ID_PROD E ADD_ITEM_CARRINHO
# nome_produto = input("digite o produto desejado:\n")
# id_produto = cc.pegar_id_prod(nome_produto)
# carrinho = cc.add_item_carrinho(Cart(prod_id = id_produto, user_id = id_user))
# if carrinho == False:
#     print("produto não encontrado!")
# else:
#     print("produto adicionado!")

### DEL_ITEM_CARRINHO
# nome_produto = input("qual produto deseja remover?\n")
# id_produto = cc.pegar_id_prod(nome_produto)
# carrinho = cc.del_item_carrinho(id_produto, id_user)
# if carrinho == False:
#     print("produto não encontrado!")
# else:
#     print("item removido!")

### LIMPAR_CARRINHO
# opcao = int(input("Deseja limpar seu carrinho?\n1 - sim\n2 - não\n"))
# if opcao == 1:
#     limpar = cc.limpar_carrinho(id_user)
#     print("carrinho vazio!")
# elif opcao == 2:
#     print("OK :(")
# else:
#     print("opcao invalida")

### VER_CARRINHO
# opcao = int(input("deseja ver carrinho?\n1 - sim\n2 - não\n"))
# if opcao == 1:
#     ver_carrinho = cc.ver_carrinho(id_user)
#     for resultado in ver_carrinho:
#         print(f'Nome: {resultado[4]} Preço: {resultado[5]}')
# elif opcao == 2:
#     print("OK :(")
# else:
#     print("opcao invalida!")

### TOTAL_COMPRA
# precos = []
# ver_carrinho = cc.ver_carrinho(id_user)
# for resultado in ver_carrinho:
#     precos.append(resultado[5])
# total = sum(precos)
# print("TOTAL DA COMPRA: R$ %.2f" % total)

### VER_PRODUTOS
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