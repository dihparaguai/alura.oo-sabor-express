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
        self._avaliacao = []
    
    # lista todos os restaurantes cadastrados
    @classmethod # informa que e um metodo que podemos utilizar sem instanciar um objeto
    def listar_todos_restaurantes(cls):
        print(f'{('nome do restaurante').ljust(20)} | {('categoria').ljust(20)} | {('avaliacao').ljust(20)} | {'status'}')
        for r in cls.restaurantes:
            print(f'{r._nome.ljust(20)} | {r._categoria.ljust(20)} | {str(r.media_avaliacoes).ljust(20)} | {(r._ativo)} ')

    # sobreescreve o atributo
    @property
    def _ativo(self):
        return 'ativado' if (self.ativo) else 'desativado'
    
    # metodo para trocar o status do restaurante usando o NOT
    def alternar_status(self):
        self.ativo = not self.ativo
    
    # self e a referencia da instancia atual que esta usando o metodo no momento
    # def __str__(self): sobrescreve a string do objeto, ao inves de mostrar a posicao na memoria
    # metodos do python sempre possuem 2 undercore antes e depois
    def __str__(self):
        return self._nome
    
    def receber_avaliacao(self, cliente, nota_avaliacao):
        nota = Avaliacao(cliente, nota_avaliacao)
        self._avaliacao.append(nota)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        qtd_notas = len(self._avaliacao)
        media = round(soma_notas / qtd_notas, 1)
        return media