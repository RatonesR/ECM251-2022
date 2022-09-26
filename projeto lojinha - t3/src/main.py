import streamlit as st

st.set_page_config(page_title="Rat Store", page_icon=":mouse:", layout="centered", initial_sidebar_state="collapsed", menu_items=None)

login_cadastro, loja, carrinho, perfil = st.tabs(["login e cadastro", "loja", "carrinho", "perfil"])

payment = ["PayPal", "Boleto Bancario", "PIX", "Visa", "Mastercard", "Diner's Club"]

SeusItens = []

with st.sidebar:
        st.sidebar.title("CARRINHO")
        with st.expander("itens"):
            st.write("seus itens")   #implementar
        st.metric(label="total da compra:", value=0)   #implementar
        option = st.selectbox(label="forma de pagamento:", options=payment)
        st.button(label="finalizar compra")    #implementar

with login_cadastro:
    col1, col2, col3 = st.columns(3)
    with col2:
        st.title("**WELCOME TRAVELER**")


    st.markdown("**INFO**")

    st.text_input("Username")
    st.text_input("Password")


    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        if st.button(label="Login"):
            st.write("login succesful!")

    with col2:
        if st.button("Cadastrar"):
            st.write("signed in!")

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
