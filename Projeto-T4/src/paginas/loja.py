from src.controllers.user_controller import UserController
from src.controllers.cart_controller import CartController
from src.paginas.estado_loja import EstadoLoja
from src.models.cart import Cart
import time
import streamlit as st


class Loja:
    def __init__(self) -> None:
        self.user_controller = UserController()
        self.cart_controller = CartController()
        self.estado_loja = EstadoLoja()
    
    def tela_loja(self):
        if "produto" not in st.session_state:
            st.session_state.produto = []
        home, produtos, carrinho, perfil = st.tabs(['Home', 'Produtos', 'Carrinho', 'Perfil'])
        with home:
            st.header("Bem vindo %s!" % st.session_state.name)
            st.header("**EM ALTA**")

            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("Aulão com Murilo")
                st.image("https://avatars.githubusercontent.com/u/24915894?v=4")
                st.info("R$ 29,99")
                with st.expander("descrição"):
                    st.write()
            with col2:
                st.markdown("Correção de Trabalho")
                st.image("https://docplayer.com.br/docs-images/79/79604769/images/16-0.jpg")
                st.info("R$ 9999,99")
                with st.expander("descrição"):
                    st.write()
            with col3:
                st.markdown("Pokemon Scarlet")
                st.image("http://cdn.shopify.com/s/files/1/0589/3970/3466/products/aa535bc65e9f1632441ffa609247e969.jpg?v=1660787455")
                st.info("R$ 299,99")
                with st.expander("descrição"):
                    st.write()

            st.header("**PROMOÇÕES**")

            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("Adiar o Projeto")
                st.image("https://images.vexels.com/media/users/3/212007/isolated/lists/307b1160d0d080207771fdde7d0c0724-ampulheta-do-magico.png")
                st.info("R$ 199,99")
                with st.expander("descrição"):
                    st.write()
            with col2:
                st.markdown("Bread Simulator")
                st.image("https://emojipedia-us.s3.amazonaws.com/source/microsoft-teams/337/bread_1f35e.png")
                st.info("R$ 4,99")
                with st.expander("descrição"):
                    st.write()
            with col3:
                st.markdown("PC gamer")
                st.image("https://img.olx.com.br/thumbs256x256/77/776270067619013.jpg")
                st.info("R$ 4499,99")
                with st.expander("descrição"):
                    st.write()
        with produtos:
            item_carrinho = None
            buscar_item = st.text_input("Busque o produto desejado")
            buscar = st.button("Buscar")
            if buscar:
                id_prod = self.cart_controller.pegar_id_prod(buscar_item)
                if id_prod != None:
                    st.session_state.produto = self.cart_controller.ver_produto(id_prod)
                    resultado1, resultado2 = st.columns(2)
                    with resultado1:
                        st.header("Resultado:")
                    with resultado2:
                        st.subheader(st.session_state.produto[1])
                        st.write(st.session_state.produto[3])
                else:
                    st.error("Nenhum item correspondente 🥺")
            add_carrinho = st.button("Adicionar ao carrinho")
            if add_carrinho:
                try:
                    item_carrinho = Cart(prod_id=st.session_state.produto[0], user_id=st.session_state.id)
                    self.cart_controller.add_item_carrinho(item_carrinho)
                    st.session_state.produto = []
                    st.success("Item adicionado!")
                except:
                    st.error("Encontre um item primeiro")
            st.title("TODOS OS PRODUTOS")
            nome, preco = st.columns(2)
            with nome:
                st.subheader("NOME")
            with preco:
                st.subheader("PREÇO")
            for resultado in range(len(self.cart_controller.ver_produtos())):
                nome_produto = self.cart_controller.ver_produtos()[resultado][1]
                preco_produto = self.cart_controller.ver_produtos()[resultado][2]
                col1, col2 = st.columns(2)
                with col1:
                    st.write(nome_produto)
                with col2:
                    st.write(preco_produto)
        with carrinho:
            st.title("MEU CARRINHO")
            ver_carrinho = self.cart_controller.ver_carrinho(st.session_state.id)
            nome_carrinho, preco_carrinho = st.columns(2)
            with nome_carrinho:
                st.subheader("Nome")
                for resultado in ver_carrinho:
                    st.write(resultado[4])
                busca = st.text_input(label="Remover item do carrinho?", placeholder="buscar produto")
            with preco_carrinho:
                precos = []
                st.subheader("Preço")
                for resultado in ver_carrinho:
                    st.write("R$ ", resultado[5])
                    precos.append(resultado[5])
                total = sum(precos)
                st.metric(label="Total a pagar", value="R$ %.2f" % total)
            opcao1, opcao2 = st.columns(2)
            with opcao1:
                remover = st.button("Remover", help="Para remover um item do carrinho digite o nome do item e pressione 'Remover'")
                if remover:
                    id_prod = self.cart_controller.pegar_id_prod(busca)
                    if id_prod != None:
                        self.cart_controller.del_item_carrinho(id_prod, st.session_state.id)
                        st.experimental_rerun()
                    else:
                        st.error("Produto não encontrado")
            with opcao2:
                pagar = st.button("Pagar")
                if pagar:
                    self.cart_controller.limpar_carrinho(st.session_state.id)
                    st.success("Compra finalizada!")
                    st.balloons()
                    with st.spinner("loading..."):
                        time.sleep(2)
                    st.experimental_rerun()
        with perfil:
            perfil1, perfil2 = st.columns(2)
            with perfil2:
                st.title("SEU PERFIL")
            image1, image2 = st.columns(2)
            with image1:
                st.image("https://cdn-icons-png.flaticon.com/128/756/756479.png", width=250)
            with image2:
                st.subheader("Nome")
                st.write(st.session_state.name)
                st.subheader("Email")
                st.write(st.session_state.email)
            opcao1, opcao2 = st.columns(2)
            with opcao1:
                sair = st.button("Sair")
                if sair:
                    self.estado_loja.estado_0()
                    st.session_state.id = None
                    st.session_state.name = None
                    st.session_state.email = None
                    st.session_state.password = None
                    st.experimental_rerun()
            with opcao2:
                editar_perfil = st.button("Editar Perfil")
                if editar_perfil:
                    self.estado_loja.estado_3()
                    st.experimental_rerun()