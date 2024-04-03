from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, descricao, tipo):
        super().__init__(nome, preco)
        self.descricao = descricao
        self.tipo = tipo

    # metodo obrigatorio devido o 'metodo abstrata' na classe pai
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.2)