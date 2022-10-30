from src.controllers.user_controller import UserController
from src.models.user import User

controller = UserController()
new_user = User("2", "Aline", "aline@aline", "aline123")
print(controller.cadastrar(new_user))