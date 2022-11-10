from src.paginas.login import Login
from src.paginas.cadastro import Cadastro
from src.paginas.loja import Loja
from src.paginas.estado_loja import EstadoLoja
import streamlit as st

login = Login()
cadastro = Cadastro()
loja = Loja()
estado_loja = EstadoLoja()

st.set_page_config(page_title="Login", page_icon=":mouse:", layout="centered", initial_sidebar_state="collapsed", menu_items=None)

estado = estado_loja.estado()

if estado == 0:
    login.tela_login()
if estado == 1:
    cadastro.tela_cadastro()
if estado == 2:
    loja.tela_loja()



# st.sidebar.title("MENU")
# with st.sidebar:
#     menu = st.selectbox('O que deseja acessar?', options=['login', 'cadastro', 'meu perfil', 'produtos', 'promoções', 'carrinho'])


# st.title("**BEM VINDO À RAT STORE! 🐀**")
# st.subheader("**A MELHOR LOJA ONLINE DO BRASIL!**")

# if menu == 'login':
#     login.tela_login()
