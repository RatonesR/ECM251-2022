from datetime import date

class Perfil:
    def __init__(self, nome, foto=""):
        self._nome = nome
        self._foto = foto
        self._data_nascimento = date.today()
        self._descricao = "Sem descricao no momento"
        self._telefone = ""