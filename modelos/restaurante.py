from modelos.avaliacao import Avaliacao

# classe
class Restaurante:
    # uma lista que guarda todos os restaurantes cadastrados
    restaurantes = []

    # metodo contrutor
    # self diz que e o atributo deste objeto
    # def __init__ diz que e o metodo construtor desta classe 
    # metodos do python sempre possuem 2 undercore antes e depois
    def __init__(self, nome, categoria):
        self._nome = nome.title() # coloque a primeira letra em maiscula
        self._categoria = categoria.upper() # coloca a categoria com todas as letras maisculas
        # utilizar o '_' para 'informar' que este atributo nao deve ser alterado pelo usuario
        self.ativo = False
        # quando um objeto for criado, ele sera adicionado a lista de restaurantes
        Restaurante.restaurantes.append(self)
        # quando um objeto for criado, sera criado uma lista para guardar suas avaliacoes
        self._avaliacao = []
    
    # self e a referencia da instancia atual que esta usando o metodo no momento
    # def __str__(self): sobrescreve a string do objeto, ao inves de mostrar a posicao na memoria
    # metodos do python sempre possuem 2 undercore antes e depois
    def __str__(self):
        return self._nome
    
    # cria uma propriedade que recebe o valor do atributo 'ativo' e utiliza string para representar seu valor
    @property
    def _ativo(self):
        return 'ativado' if (self.ativo) else 'desativado'
    
    # cria uma propriedade que realiza a media das avaliacoes
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        # realiza a soma de cada nota, dentro do objeto avaliacoes na lista de avaliacoes
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        qtd_notas = len(self._avaliacao)
        media = round(soma_notas / qtd_notas, 1)
        return media
    
    # metodo para trocar o status do restaurante usando o NOT
    def alternar_status(self):
        self.ativo = not self.ativo
    
    # metodo que recebe uma avaliacao, e cria um objeto com ela, depois adiciona esse objeto na lista de avaliacoes
    def receber_avaliacao(self, cliente, nota_avaliacao):
        nota = Avaliacao(cliente, nota_avaliacao)
        self._avaliacao.append(nota)
    
    # lista todos os restaurantes cadastrados
    @classmethod # informa que e um metodo que podemos utilizar sem instanciar um objeto
    def listar_todos_restaurantes(cls):
        print(f'{('nome do restaurante').ljust(20)} | {('categoria').ljust(20)} | {('avaliacao').ljust(20)} | {'status'}')
        for r in cls.restaurantes:
            # para usar o 'ljust()' a variavel precisa ser do tipo string
            print(f'{r._nome.ljust(20)} | {r._categoria.ljust(20)} | {str(r.media_avaliacoes).ljust(20)} | {(r._ativo)} ')
