from src.controllers.app_controller import Application
from src.controllers.user_controller import UserController
from src.controllers.cart_controller import CartController
import streamlit as st


st.set_page_config(page_title="Rat Store", page_icon=":mouse:", layout="centered", initial_sidebar_state="collapsed", menu_items=None)

app = Application()
user_controller = UserController()
cart_controller = CartController()
estado_login = False

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
    usuario = user_controller.checklogin(name, password)
    st.write(usuario)
    # if usuario != None:
    #     user_id = user_controller.pegar_id(input_name, input_password)
    #     user_name = user_controller.pegar_nome(user_id)
    #     user_email = user_controller.pegar_email(user_id)
    #     st.write(user_id, user_name, user_email)
    #     st.write("login successful!")
    # else:
    #     st.write("Incorrect username or password")

# if botao_cadastrar:
#     st.write("em construção")

