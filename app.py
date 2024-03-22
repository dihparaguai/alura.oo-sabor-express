# da pasta 'modelos', do arquivo 'restaurante', importe a classe 'Restaurante'
from modelos.restaurante import Restaurante

# instanciacao da classe com metodo construtor
restaurante_praca = Restaurante('praça', 'gourmet')
restaurante_pizza = Restaurante('pizza Express', 'italiana')
restaurante_mexinaco = Restaurante('Mexican Food', 'mexinaca') 

# colocando os restaurantes numa lista
restaurantes = [restaurante_praca, restaurante_pizza]

# metodo 'vars', mostra os atributos do objeto em forma de 'dicionario'
# se nao usado, sera mostrado a posicao deste objeto na memoria fisica
print()
print('dicionario do objeto')
print(vars(restaurante_praca))
print(vars(restaurante_pizza))

# depois de aplicar o __str__ (self) foi sobrescrito a string do objeto, ao inves de mostrar a posicao na memoria 
print()
print('string do objeto sobrescrita')
print(restaurante_praca)
print(restaurante_pizza)

# print()
# print('lisgem com todos os restaurantes cadastrados')
# Restaurante.listar_todos_restaurantes()

restaurante_praca.receber_avaliacao('diego', 10)
restaurante_praca.receber_avaliacao('parguai', 9)
restaurante_praca.receber_avaliacao('carvalho', 6)
restaurante_praca.receber_avaliacao('rodrigo', 4)

# trocando o status do restaurante
restaurante_praca.alternar_status()

# trocando valores aos atributos da classe
restaurante_praca._nome = 'estadio'
restaurante_pizza._categoria = 'bola'

def main():
    Restaurante.listar_todos_restaurantes()

if __name__ == "__main__":
    main()