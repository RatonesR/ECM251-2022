import streamlit as st

st.set_page_config(page_title="Rat Store", page_icon=":mouse:", layout="centered", initial_sidebar_state="collapsed", menu_items=None)

login_cadastro, loja, carrinho, perfil = st.tabs(["login e cadastro", "loja", "carrinho", "perfil"])

payment = ["PayPal", "Boleto Bancario", "PIX", "Visa", "Mastercard", "Diner's Club"]

with st.sidebar:
        st.sidebar.title("CARRINHO")
        with st.expander("itens"):
            st.write("seus itens")
        st.write("total da compra:")
        option = st.selectbox(label="forma de pagamento:", options=payment)
        st.button(label="pagar")

with login_cadastro:
    col1, col2, col3 = st.columns(3)
    with col2:
        st.title("**WELCOME TRAVELER**")


    st.markdown("**LOGIN**")

    st.text_input("Username")
    st.text_input("Password")


    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        if st.button(label="Login"):
            st.write("login succesful!")

    with col2:
        if st.button("Cadastrar"):
            st.write("signed in!")

