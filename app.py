# da pasta 'modelos', do arquivo 'restaurante', importe a classe 'Restaurante'
from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

# instanciacao da classe com metodo construtor
restaurante_praca = Restaurante('praça', 'gourmet')
restaurante_pizza = Restaurante('pizza Express', 'italiana')
restaurante_mexinaco = Restaurante('Mexican Food', 'mexinaca') 

# colocando os restaurantes numa lista
restaurantes = [restaurante_praca, restaurante_pizza]

# metodo 'vars', mostra os atributos do objeto em forma de 'dicionario'
# se nao usado, sera mostrado a posicao deste objeto na memoria fisica
print('dicionario do objeto')
print(vars(restaurante_praca))
print(vars(restaurante_pizza))
print()

# depois de aplicar o __str__ (self) foi sobrescrito a string do objeto, ao inves de mostrar a posicao na memoria 
print('string do objeto sobrescrita')
print(restaurante_praca)
print(restaurante_pizza)
print()

# print('lisgem com todos os restaurantes cadastrados')
# Restaurante.listar_todos_restaurantes()
# print()

restaurante_praca.receber_avaliacao('diego', 10)
restaurante_praca.receber_avaliacao('parguai', 9)
restaurante_praca.receber_avaliacao('carvalho', 6)
restaurante_praca.receber_avaliacao('rodrigo', 4)

# trocando o status do restaurante
restaurante_praca.alternar_status()

# trocando valores aos atributos da classe
restaurante_praca._nome = 'estadio'
restaurante_pizza._categoria = 'bola'
restaurante_praca._nome = 'pracinha'

bebida_suco = Bebida('suco', 3.5, 'enorme')
prato_lasanha = Prato('lasanha', 27, 'lasanha a bolonhesa')
sobremesa_sorvete = Sobremesa('sorvete', 10, 'chocolate', 'palito')

bebida_suco.aplicar_desconto()
prato_lasanha.aplicar_desconto()
sobremesa_sorvete.aplicar_desconto()

# neste caso, a funcao 'adicionar_cardapio' e uma funcao que funciona para varias classes derivadas(herança) de 'ItemCardapio'
restaurante_praca.adicionar_cardapio(bebida_suco)
restaurante_praca.adicionar_cardapio(prato_lasanha)
restaurante_praca.adicionar_cardapio(sobremesa_sorvete)

def main():
    Restaurante.listar_todos_restaurantes()
    restaurante_praca.exibir_itens_cardapio

if __name__ == "__main__":
    main()