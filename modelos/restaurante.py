# classe
class Restaurante:
    # metodo contrutor
    # self diz que e o atributo deste objeto
    # def __init__ diz que e o metodo construtor desta classe 
    # metodos do python sempre possuem 2 undercore antes e depois
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

    # self e a referencia da instancia atual que esta usando o metodo no momento
    # def __str__(self): sobrescreve a string do objeto, ao inves de mostrar a posicao na memoria
    # metodos do python sempre possuem 2 undercore antes e depois
    def __str__(self):
        return self.nome


# instanciacao da classe com metodo construtor
restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')


# trocando valores aos atributos da classe
restaurante_praca.nome = 'Estadio'
restaurante_praca.categoria = 'Bola'

# colocando os restaurantes numa lista
restaurantes = [restaurante_praca, restaurante_pizza]

# metodo vars, mostra os atributos do objeto em forma de 'dicionario'
# se nao usado, sera mostrado a posicao deste objeto na memoria fisica
print()
print('dicionario do objeto')
print(vars(restaurante_praca))
print(vars(restaurante_pizza))

# depois de aplicar o __str__ (self): foi sobrescrito a string do objeto, ao inves de mostrar a posicao na memoria 
print()
print('string do objeto sobrescrita')
print(restaurante_praca)
print(restaurante_pizza)

