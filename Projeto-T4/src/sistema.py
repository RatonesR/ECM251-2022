from src.controllers.app_controller import Application
import streamlit as st

st.set_page_config(page_title="Rat Store", page_icon=":mouse:", layout="centered", initial_sidebar_state="collapsed", menu_items=None)

app = Application()
estado_login = None

st.title("**WELCOME TRAVELER**")
with st.form(key="verify_user"):
    st.markdown("**INFO**")
    input_name = st.text_input(label="Username")
    input_password = st.text_input(label="Password")
    input_button_submit = st.form_submit_button("Login")

    estado_login = app.login(input_name, input_password)

    if estado_login != None:
        st.write("login successful!")
    else:
        st.write("Incorrect username or password")
