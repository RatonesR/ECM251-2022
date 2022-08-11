from xmlrpc.client import FastUnmarshaller


class Item():
    def __init__(self, preco, nome,  descricao=None):
        self._preco = preco
        self._nome = nome
        self._descricao = descricao
    def get_nome(self):
        return self._nome
    def get_preco(self):
        return self._preco
    def get_descricao(self):
        return self._descricao
    def __str__(self):
        return f'Nome: {self._nome} Preco: R${self._preco}'
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Item):
            return self._nome == __o.get_nome()
        return False
