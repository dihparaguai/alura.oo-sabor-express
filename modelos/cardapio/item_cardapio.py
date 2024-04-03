from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    # cria uma (interface) 'metodo abstatrato', que obriga todas as classes filhas a terem este metodo implementado
    @abstractmethod
    def aplicar_desconto(self):
        pass