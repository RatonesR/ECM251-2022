import streamlit as st

st.set_page_config(page_title="Rat Store", page_icon=":mouse:", layout="centered", initial_sidebar_state="collapsed", menu_items=None)


with st.sidebar:
    st.sidebar.button("LOGIN")
    st.sidebar.button("LOJA")
    st.sidebar.button("CARRINHO")
    st.sidebar.button("PERFIL")
    st.sidebar.button("SAIR")

col1, col2, col3 = st.columns(3)
with col2:
    st.title("**WELCOME TRAVELER**")


st.markdown("**LOGIN**")

st.text_input("Username", "")
st.text_input("Password", "")


col1, col2, col3, col4, col5 = st.columns(5)

def logar():
    st.write("login succesful!")

with col1:
    login = st.button(label="Login", on_click=logar)
    st.write(login)

with col2:
    cadastrar = st.button("Cadastrar")
    st.write(cadastrar)

