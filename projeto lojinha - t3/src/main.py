import streamlit as st
from controllers.user_controller import UserController as uc

st.set_page_config(page_title="Rat Store", page_icon=":mouse:", layout="centered", initial_sidebar_state="collapsed", menu_items=None)

login, cadastro, loja, carrinho = st.tabs(["login", "cadastro", "loja", "carrinho"])

payment = ["PayPal", "Boleto Bancario", "PIX", "Visa", "Mastercard", "Diner's Club"]

SeusItens = []
Usuario_nome = ["Luiz", "opa"]
Usuario_email = ["Luiz@gmail.com", "opa@opa"]
Usuario_senha = ["Luiz", "opa"]

with st.sidebar:
    st.sidebar.title("PERFIL")
    col1, col2, col3 = st.columns(3)
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/616/616569.png", caption="imagem de perfil", width=100)
    st.write("Nome: ", Usuario_nome[0])
    st.write("Email: ", Usuario_email[0])
    log_out = st.button(label="logout")

    if log_out:
        del(Usuario_nome[0])
        del(Usuario_email[0])
        del(Usuario_senha[0])
        st.write("Logged out!")

with login:
    st.title("**WELCOME TRAVELER**")

    with st.form(key="verify_user"):
        st.markdown("**INFO**")
        input_name = st.text_input(label="Username")
        input_password = st.text_input(label="Password")
        input_button_submit = st.form_submit_button("Login")

        if input_button_submit:
            if uc.checkLogin(input_name, input_password, None):
                st.write("Login successful!")
            else:
                st.write("Incorrect username or password")
        else:
            st.write("Press to submit")

with cadastro:
    st.title("Preencha suas Informações:")
    with st.form(key="include_user"):
        input_name = st.text_input(label="Username")
        input_email = st.text_input(label="Email")
        input_password = st.text_input(label="Password")
        input_button_submit = st.form_submit_button("Cadastrar")

    if input_button_submit:
        st.write("Signed In!")

with loja:

    st.title("BEM VINDO À NOSSA LOJA")

    st.header("**EM ALTA**")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("Aulão com Murilo")
        st.image("https://avatars.githubusercontent.com/u/24915894?v=4")
        st.info("R$ 29,99")
    with col2:
        st.markdown("Correção de Trabalho")
        st.image("https://docplayer.com.br/docs-images/79/79604769/images/16-0.jpg")
        st.info("R$ 9999,99")
    with col3:
        st.markdown("Pokemon Scarlet")
        st.image("https://styles.redditmedia.com/t5_5x8srd/styles/communityIcon_ltry6sr9afk81.png?width=256&s=34d711da385cf952b463e85ddc5d88d5f9249602")
        st.info("R$ 299,99")

    st.markdown("**PROMOÇÕES**")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("Adiar o Projeto")
        st.image("https://images.vexels.com/media/users/3/212007/isolated/lists/307b1160d0d080207771fdde7d0c0724-ampulheta-do-magico.png")
        st.info("R$ 199,99")
    with col2:
        st.markdown("Bread Simulator")
        st.image("https://emojipedia-us.s3.amazonaws.com/source/microsoft-teams/337/bread_1f35e.png")
        st.info("R$ 4,99")
    with col3:
        st.markdown("PC gamer")
        st.image("https://img.olx.com.br/thumbs256x256/77/776270067619013.jpg")
        st.info("R$ 4499,99")

with carrinho:
    st.title("**SEUS ITENS**")
    remover = st.selectbox(label="Remover Item", options=SeusItens)
