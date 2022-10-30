import streamlit as st
from src.controllers.user_controller import UserController
from src.models.user import User
import uuid

class Application:
    def __init__(self):
        self.user_controller = UserController()