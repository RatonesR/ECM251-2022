from src.paginas.login import Login
from src.paginas.cadastro import Cadastro
from src.paginas.loja import Loja
from src.paginas.editar_perfil import EditarPerfil
from src.paginas.estado_loja import EstadoLoja
import streamlit as st

login = Login()
cadastro = Cadastro()
loja = Loja()
editar = EditarPerfil()
estado_loja = EstadoLoja()

st.set_page_config(page_title="Login", page_icon=":mouse:", layout="centered", initial_sidebar_state="collapsed", menu_items=None)

estado = estado_loja.estado()

if estado == 0:
    login.tela_login()
if estado == 1:
    cadastro.tela_cadastro()
if estado == 2:
    loja.tela_loja()
if estado == 3:
    editar.tela_edicao()
