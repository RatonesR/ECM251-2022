from src.dao.user_dao import UserDAO

menu = int(input("DIGITE:\n1: cadastrar \n2: login\n"))

if menu == 1:
    #CADASTRA NOVO USUARIO
    nome = input("digite seu nome: ")
    email = input("digite seu email: ")
    senha = input("digite sua senha: ")
    cadastro = UserDAO.get_instance().cadastrar(nome, email, senha)
if menu == 2:
    #VERIFICA SE O USUARIO E SENHA EXISTEM
    nome = input("digite seu nome: ")
    senha = input("digite sua senha: ")
    login = UserDAO.get_instance().pegarlogin(nome, senha)
    if login != None:
        print("login successful!")
    else:
        print("Incorrect username or password!")