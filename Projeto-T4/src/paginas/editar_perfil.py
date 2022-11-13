from src.controllers.user_controller import UserController
from src.paginas.estado_loja import EstadoLoja
import streamlit as st

class EditarPerfil:
    def __init__(self) -> None:
        self.user_controller = UserController()
        self.estado_loja = EstadoLoja()

    def tela_edicao(self):
        voltar = st.button("voltar")
        if voltar:
            self.estado_loja.estado_2()
            st.experimental_rerun()
        perfil1, perfil2 = st.columns(2)
        with perfil2:
            st.title("PERFIL")
        image1, image2 = st.columns(2)
        with image1:
            st.image("https://cdn-icons-png.flaticon.com/128/756/756479.png", width=250)
        with image2:
            nome = st.text_input(label="Nome", value=st.session_state.name)
            email = st.text_input(label="Email", value=st.session_state.email)
            senha = st.text_input(label="Senha", value=st.session_state.password)
        opcao1, opcao2 = st.columns(2)
        with opcao1:
            excluir_conta = st.button("Excluir Conta")
            if excluir_conta:
                self.user_controller.excluir_conta(st.session_state.id)
                st.session_state.id = None
                st.session_state.name = None
                st.session_state.email = None
                st.session_state.password = None
                self.estado_loja.estado_0()
                st.experimental_rerun()
        with opcao2:
            salvar_alteracoes = st.button("Salvar Alterações")
            if salvar_alteracoes:
                self.user_controller.editar_perfil(nome, email, senha, st.session_state.id)
                st.session_state.name = nome
                st.session_state.email = email
                st.session_state.password = senha
                self.estado_loja.estado_2()
                st.experimental_rerun()