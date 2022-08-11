from item import Item
from carrinho import Carrinho

item1 = Item(199, 'Dark Souls')
item2 = Item(
    preco=350,
    nome='Dark Souls',
    descricao='Vai sofrer muito!'
)

carrinho = Carrinho()

carrinho.adicionar(item1)
carrinho.adicionar(item2)

print('Tamanho: ', carrinho.get_tamanho())
print('Valor total: ', carrinho.get_valor_total())