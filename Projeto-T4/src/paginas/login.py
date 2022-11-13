from src.controllers.user_controller import UserController
from src.paginas.estado_loja import EstadoLoja
import time
import streamlit as st

class Login:
    if "name" not in st.session_state:
        st.session_state.name = None
    if "email" not in st.session_state:
        st.session_state.email = None
    if "password" not in st.session_state:
        st.session_state.password = None
    if "id" not in st.session_state:
        st.session_state.id = None

    def __init__(self) -> None:
        self.user_controller = UserController()
        self.estado_loja = EstadoLoja()
        
    def tela_login(self):
        st.title("**WELCOME TRAVELER**")
        st.markdown("**FAÇA SEU LOGIN**")
        name = st.text_input(label="Username")
        password = st.text_input(label="Password")
        col1, col2, col3 = st.columns(3)
        with col1:
            botao_login = st.button(label="Login")
        with col3:
            botao_cadastrar = st.button("Cadastrar", help="Ainda não possui uma conta na nossa loja? Cadastre-se aqui!")
        if botao_login:
            usuario = self.user_controller.checklogin(name, password)
            if usuario != None:
                st.session_state.id = self.user_controller.pegar_id(name, password)
                st.session_state.name = self.user_controller.pegar_nome(st.session_state.id)
                st.session_state.email = self.user_controller.pegar_email(st.session_state.id)
                st.session_state.password = self.user_controller.pegar_senha(st.session_state.id)
                st.success("login successful!")
                with st.spinner("loading..."):
                    time.sleep(1)
                self.estado_loja.estado_2()
                st.experimental_rerun()
            else:
                st.error("Incorrect username or password")
        if botao_cadastrar:
            self.estado_loja.estado_1()
            st.experimental_rerun()