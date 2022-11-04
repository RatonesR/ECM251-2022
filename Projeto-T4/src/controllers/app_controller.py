import streamlit as st
from src.controllers.user_controller import UserController
from src.controllers.cart_controller import CartController
from src.models.user import User
from src.models.cart import Cart
from src .models.products import Products
import uuid

class Application:
    def __init__(self):
        self.user_controller = UserController()
        self.cliente_pedido_atual = None