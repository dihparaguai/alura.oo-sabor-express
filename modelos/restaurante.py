# classe
class Restaurante:
    # uma lista que guarda todos os restaurantes cadastrados
    restaurantes = []

    # metodo contrutor
    # self diz que e o atributo deste objeto
    # def __init__ diz que e o metodo construtor desta classe 
    # metodos do python sempre possuem 2 undercore antes e depois
    def __init__(self, _nome, _categoria):
        self.nome = _nome.title() # coloque a primeira letra em maiscula
        self.categoria = _categoria.upper() # coloca a categoria com todas as letras maisculas
        # utilizar o '_' para 'informar' que este atributo nao deve ser alterado pelo usuario
        self._ativo = False
        # quando um objeto for criado, ele sera adicionado a lista de restaurantes
        Restaurante.restaurantes.append(self)
    
    # lista todos os restaurantes cadastrados
    @classmethod # informa que e um metodo que podemos utilizar sem instanciar um objeto
    def listar_todos_restaurantes(cls):
        print(f'{('nome do restaurante').ljust(20)} | {('categoria').ljust(20)} | {'status'}')
        for r in cls.restaurantes:
            print(f'{r.nome.ljust(20)} | {r.categoria.ljust(20)} | {(r.ativo)} ')
    
    # sobreescreve o atributo
    @property
    def ativo(self):
        return 'ativado' if (self._ativo) else 'desativado'
    
    # metodo para trocar o status do restaurante usando o NOT
    def alternar_status(self):
        self._ativo = not self._ativo
    
    # self e a referencia da instancia atual que esta usando o metodo no momento
    # def __str__(self): sobrescreve a string do objeto, ao inves de mostrar a posicao na memoria
    # metodos do python sempre possuem 2 undercore antes e depois
    def __str__(self):
        return self.nome

# instanciacao da classe com metodo construtor
restaurante_praca = Restaurante('praça', 'gourmet')
restaurante_pizza = Restaurante('pizza Express', 'italiana')

# trocando valores aos atributos da classe
restaurante_praca.nome = 'estadio'
restaurante_pizza.categoria = 'bola'

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

# trocando o status do restaurante
restaurante_praca.alternar_status()

print()
print('lisgem com todos os restaurantes cadastrados')
Restaurante.listar_todos_restaurantes()