from src.paginas.login import Login
from src.paginas.cadastro import Cadastro
from src.paginas.estado_loja import EstadoLoja
import streamlit as st

login = Login()
cadastro = Cadastro()
estado_loja = EstadoLoja()

st.set_page_config(page_title="Login", page_icon=":mouse:", layout="centered", initial_sidebar_state="collapsed", menu_items=None)

while estado_loja.estado() == 0:
    login.tela_login()
while estado_loja.estado() == 1:
    cadastro.tela_cadastro()