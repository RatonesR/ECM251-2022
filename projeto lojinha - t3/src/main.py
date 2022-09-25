import streamlit as st

st.set_page_config(page_title="Rat Store", page_icon=":mouse:", layout="centered", initial_sidebar_state="collapsed", menu_items=None)


col1, col2, col3 = st.columns(3)
with col2:
    st.title("**WELCOME TRAVELER**")


st.markdown("**LOGIN**")

st.text_input("Username", "")
st.text_input("Password", "")


col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    login = st.button("Login")
    st.write(login)
    if login:
        st.caption("login successful")
    else:
        st.caption("wrong username or password")

with col2:
    cadastrar = st.button("Cadastrar")
    st.write(cadastrar)

