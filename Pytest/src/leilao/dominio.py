import sys


class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    def propoe_lance(self, leilao, valor):
        if valor > self.__carteira:
            raise ValueError('Não pode propor um lance com o valor menor que o da carteira.')

        lance = Lance(self, valor)
        leilao.propoe(lance)

        self.__carteira -= valor

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return  self.__carteira


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

    def propoe(self, lance: Lance):  # anotação (type hint), só para ajudar a n se perder no código
        # se a lista estiver vazia "not lances"
        # -1: acesso ao último elemento da lista
        if not self.__lances or self.__lances[-1].usuario != lance.usuario and lance.valor > self.__lances[-1].valor:
            if lance.valor > self.maior_lance:
                self.maior_lance = lance.valor
            if lance.valor < self.menor_lance:
                self.menor_lance = lance.valor

            self.__lances.append(lance)
        else:
            raise ValueError('Erro ao propor lance.')

    @property
    def lances(self):
        return self.__lances[:]  # devolve copia rasa da lista





