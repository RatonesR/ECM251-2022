import streamlit as st

class EstadoLoja:
    if "state" not in st.session_state:
        st.session_state.state = 0

    def estado(self):
        return st.session_state.state

    def estado_0(self):
        st.session_state.state = 0
        return st.session_state.state

    def estado_1(self):
        st.session_state.state = 1
        return st.session_state.state

    def estado_2(self):
        st.session_state.state = 2
        return st.session_state.state

    def estado_3(self):
        st.session_state.state = 3
        return st.session_state.state