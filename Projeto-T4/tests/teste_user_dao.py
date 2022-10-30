from src.dao.user_dao import UserDAO

menu = int(input("DIGITE:\n1: cadastrar \n2: login\n3: excluir conta\n"))

if menu == 1:
    #CADASTRA NOVO USUARIO
    name = input("digite seu nome: ")
    email = input("digite seu email: ")
    password = input("digite sua senha: ")
    user = UserDAO.get_instance().cadastrar(name, email, password)
    if user == True:
        print("Signed in!")
    else:
        print("Sign in failed!")
if menu == 2:
    #VERIFICA SE O USUARIO E SENHA EXISTEM
    name = input("digite seu nome: ")
    password = input("digite sua senha: ")
    login = UserDAO.get_instance().checklogin(name, password)
    if login != None:
        print("login successful!")
    else:
        print("Incorrect username or password!")
if menu == 3:
    #EXCLUI CONTA EXISTENTE
    name = input("digite seu nome: ")
    email = input("digite seu email: ")
    password = input("digite sua senha: ")
    excluir = UserDAO.get_instance().excluir_conta(name, email, password)
    if excluir == True:
        print("Account deleted!")
    else:
        print("Invalid user!")