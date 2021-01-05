import sys

class Usuario:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []  # lista
        self.maior_lance = sys.float_info.min  # pega as informações do float (menor valor)
        self.menor_lance = sys.float_info.max  # maior valor

    def propoe(self, lance: Lance): # anotação (type hint), só para ajudar a n se perder no código
        # -1: acesso ao último elemento da lista
        if not self.__lances or self.__lances[-1].usuario != lance.usuario:  # se a lista estiver vazia "not lances"
            if lance.valor > self.maior_lance:
                self.maior_lance = lance.valor
            if lance.valor < self.menor_lance:
                self.menor_lance = lance.valor

        self.__lances.append(lance)

    @property
    def lances(self):
        return self.__lances[:]  # devolve copia rasa da lista





