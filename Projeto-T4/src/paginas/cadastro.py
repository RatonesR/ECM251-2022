from src.controllers.user_controller import UserController
from src.paginas.estado_loja import EstadoLoja
from src.models.user import User
import streamlit as st

class Cadastro:
    def __init__(self) -> None:
        self.user_controller = UserController()
        self.estado_loja = EstadoLoja()

    def tela_cadastro(self):
        st.title("**CADASTRE-SE AQUI**")
        st.markdown("**INFO**")
        name = st.text_input(label="Username")
        email = st.text_input(label="email")
        password = st.text_input(label="Password")
        col1, col2, col3 = st.columns(3)
        with col1:
            botao_cadastrar = st.button(label="Cadastrar", help="Faça seu login aqui!")
        with col3:
            botao_logar = st.button("Voltar para o Login")
        if botao_cadastrar:
            user = User(name = name, email = email, password = password)
            validar = user.validar_user()
            if validar == True:
                self.user_controller.cadastrar(User(name = name, email = email, password = password))
                self.estado_loja.estado_0()
                st.experimental_rerun()
            elif validar == False:
                st.error("Preencha todos os campos!")
        if botao_logar:
            self.estado_loja.estado_0()
            st.experimental_rerun()