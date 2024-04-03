from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho

    # metodo obrigatorio devido o 'metodo abstrata' na classe pai
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.5)