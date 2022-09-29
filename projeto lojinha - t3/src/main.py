from os import write
import streamlit as st
from controllers.user_controller import UserController as uc

st.set_page_config(page_title="Rat Store", page_icon=":mouse:", layout="centered", initial_sidebar_state="collapsed", menu_items=None)

login, cadastro, loja, carrinho, teste = st.tabs(["login", "cadastro", "loja", "carrinho", "teste"])

payment = ["PayPal", "Boleto Bancario", "PIX", "Visa", "Mastercard", "Diner's Club"]

precos = [
    29.99,
    9999.99,
    299.99,
    199.99,
    4.99,
    4499.99
]

produtos = [
    "Aulão com Murilo",
    "Correção de Trabalho",
    "Pokemon Scarlet",
    "Adiar o Projeto",
    "Bread Simulator",
    "PC gamer"
]

# Usuario_nome = ["Luiz", "opa"]
# Usuario_email = ["Luiz@gmail.com", "opa@opa"]
# Usuario_senha = ["Luiz", "opa"]

with teste:
    st.write("oi")
    #login

    # nome_login = st.text_input(label="username")
    # email_login = st.text_input(label="email")
    # senha_login = st.text_input(label="senha")
    # lista_login = [nome_login, email_login, senha_login]
    # botao2 = st.button("Login")


    # if botao2:
    #     for i in st.session_state.chave:
    #         lista_teste = st.session_state.chave[i]
    #         if lista_teste == lista_login:
    #             st.write("sucesso")
    #             break
    #         else:
    #             st.write("deu ruim")


    #comprar

    # opcao = st.selectbox("Buscar", options=("Aulão com Murilo",
    # "Correção de Trabalho",
    # "Pokemon Scarlet",
    # "Adiar o Projeto",
    # "Bread Simulator",
    # "PC gamer"
    # ))

    # if "carrinho_produto" not in st.session_state:
    #     st.session_state.carrinho_produto = []
    # if "carrinho_preco" not in st.session_state:
    #     st.session_state.carrinho_preco = []

    # add_cart = st.button("adicionar ao carrinho")

    # if add_cart:
    #     st.session_state.carrinho_produto.append(opcao)
    #     st.session_state.carrinho_preco.append(precos[produtos.index(opcao)])



with login:
    st.title("**WELCOME TRAVELER**")

    with st.form(key="verify_user"):
        st.markdown("**INFO**")
        input_name = st.text_input(label="Username")
        input_password = st.text_input(label="Password")
        input_button_submit = st.form_submit_button("Login")

        if input_button_submit:
            if input_name in st.session_state.chave:
                st.write("Login successful!")
            else:
                st.write("Incorrect username or password")
        else:
            st.write("Press to submit")

with cadastro:
    st.title("Preencha suas Informações:")

    nome = st.text_input(label="Username")
    email = st.text_input(label="Email")
    senha = st.text_input(label="Password")
    botao1 = st.button("cadastro")

    if "chave" not in st.session_state:
        st.session_state.chave = [[" "," "," "]]

    if botao1:
        st.session_state.chave.append([nome, email, senha])
        st.write("Cadastrado!")  

with loja:
    # st.selectbox("Buscar", options=("Aulão com Murilo",
    # "Correção de Trabalho",
    # "Pokemon Scarlet",
    # "Adiar o Projeto",
    # "Bread Simulator",
    # "PC gamer"
    # ))

    st.title("BEM VINDO À NOSSA LOJA")

    opcao = st.selectbox("Buscar", options=("Aulão com Murilo",
    "Correção de Trabalho",
    "Pokemon Scarlet",
    "Adiar o Projeto",
    "Bread Simulator",
    "PC gamer"
    ))

    if "carrinho_produto" not in st.session_state:
        st.session_state.carrinho_produto = []
    if "carrinho_preco" not in st.session_state:
        st.session_state.carrinho_preco = []

    add_cart = st.button("adicionar ao carrinho")

    if add_cart:
        st.session_state.carrinho_produto.append(opcao)
        st.session_state.carrinho_preco.append(precos[produtos.index(opcao)])

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

    st.header("**PROMOÇÕES**")

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
    col01, col02 = st.columns(2)
    for i in range(len(st.session_state.carrinho_produto)):
        st.empty()
        col01.write(st.session_state.carrinho_produto[i])
        col02.write(st.session_state.carrinho_preco[i])

    botao_remover = st.button("remover", help="remove o último item do carrinho")

    col1, col2, col3 = st.columns(3)
    preco_total = col1.metric("PREÇO TOTAL:", value=sum(st.session_state.carrinho_preco))
    forma_pagamento = col2.selectbox("selecione forma de pagamento", options=("PayPal", "Boleto Bancário", "PIX", "Crédito", "Débito"))
    pagar_tudo = st.button("pagar")
    if pagar_tudo:
        st.write("você gastou dindin")
    if botao_remover:
        if(len(st.session_state.carrinho_produto)!=0 and len(st.session_state.carrinho_preco)!=0):
            removed_element = st.session_state.carrinho_produto.pop(-1)
            removed_element = st.session_state.carrinho_preco.pop(-1)
            col01.info("Recarregue a página para atualizar o carrinho")

with st.sidebar:
    st.sidebar.title("PERFIL")
    col1, col2, col3 = st.columns(3)
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/616/616569.png", caption="imagem de perfil", width=100)
    st.write("Nome: ", st.session_state.chave[-1][0])
    st.write("Email: ", st.session_state.chave[-1][1])
    logout = st.button(label="logout")

    if logout:
        st.write("Logged out!")



