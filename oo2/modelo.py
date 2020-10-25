class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()# põe em letra maiúscula (como um título)
        self.ano = ano
        self._likes = 0 # um underline torna os atributos visíveis às classes filhas

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

class Filme(Programa): # programa é a classe pai que eu Filme herdou
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano) # super() herda os atributos da classe pai
        self.duracao = duracao

# pass #criei a classe sem o construtor __init__ ou outra implementação e termino ela

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

vingadores = Filme('vingadores: guerra infinita', 2018, 160)
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

friends = Serie('friends', 1994, 10)
friends.dar_likes()
friends.dar_likes()

print(f'{vingadores.nome} - {vingadores.duracao} - {vingadores.likes}')
print(f'Nome: {friends.nome} - {friends.temporadas} - {friends.likes}')

# capitalize()#põe a primeira palavra da frase em letra maiúscula