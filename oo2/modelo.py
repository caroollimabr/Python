from abc import ABC #abstract base classes
from collections.abc import MutableSequence



class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()# põe em letra maiúscula (como um título)
        self.ano = ano
        self._likes = 0 # um underline torna os atributos visíveis às classes filhas

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def __str__(self): # retornará uma representação string do obj
        print(f'{self._nome} - {self.ano} - {self._likes} likes')

class Filme(Programa): # programa é a classe pai que eu Filme herdou
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano) # super() herda os atributos da classe pai
        self.duracao = duracao

    def __str__(self):
        return (f'{self._nome} - {self.ano} - {self.duracao} min. - {self._likes} likes')

# pass #criei a classe sem o construtor __init__ ou outra implementação e termino ela

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} likes'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    @property
    def __len__(self):
        return len(self._programas)

#    def tamanho(self): ---não preciso mais porque Playlist está herdando a classe list
#        return len(self.programas) # len() retornará o tamanho

vingadores = Filme('vingadores: guerra infinita', 2018, 149)
friends = Serie('friends', 1994, 10)
titanic = Filme('titanic', 1998, 195)
cobra_kai = Serie ('cobra kai', 2018, 3)

cobra_kai.dar_like()
titanic.dar_like()
titanic.dar_like()
titanic.dar_like()
titanic.dar_like()
vingadores.dar_like()
vingadores.dar_like()
friends.dar_like()
friends.dar_like()
friends.dar_like()

filmes_e_series = [cobra_kai, titanic, vingadores, friends] #list
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho do playlist: {len(playlist_fim_de_semana.listagem)}')#len() - length: percorre a lista de programas

print(playlist_fim_de_semana[0])


for programa in playlist_fim_de_semana:
    print(programa) #na hora do imprime, ele vai escolher qual será: o imprime da série ou do filme

#    if hasattr(programa, 'duracao'): #hasattr(obj, nome): has attribute, se tiver algo, ele retorna algo. Se não, retorna outra coisa
#        detalhes = programa.duracao
#    else:
#        detalhes = programa.temporadas
#
#    print(f'{programa.nome} - {detalhes} - {programa.likes}')

# capitalize()#põe a primeira palavra da frase em letra maiúscula