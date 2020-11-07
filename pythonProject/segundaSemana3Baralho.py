from random import shuffle

class Carta:  # representa uma carta do baralho
    def __init__(self, valor, naipe):  # inicializa o valor e o naipe da carta
        self.valor = valor
        self.naipe = naipe

    def get_rank(self):  # retorna valor
        return self.valor

    def get_naipe(self):  # retorna naipe
        return self.naipe

    def __repr__(self):  # retorna representação de string canônica Carta(valor, naipe)
        return "Carta ('{}', '{}')".format(self.valor, self.naipe)

    def __eq__(self, outra):  # self = outra se o valor e o naipe forem os mesmos
        return self.valor == outra.valor and self.naipe == outra.naipe

class Baralho:  # representa um baralho de 52 cartas
    valores = {'2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'}
    naipes = {'\u2660', '\u2661', '\u2662', '\u2663'}  # 4 símbolos Unicode representando os 4 naipes

    def __init__(self, lista_cartas = None):  # inicializa o baralho de 52 cartas
        if lista_cartas != None:  # entra o baralho fornecido
            self.baralho = lista_cartas
        else:
            self.baralho = []

        for naipe in Baralho.naipes:  # para cada naipe do Baralho
            for valor in Baralho.valores:  # para cada valor do Baralho
                self.baralho.append(Carta(valor, naipe))

    def distribui_carta(self):  # (remove e retorna) carta do topo do baralho
            return self.baralho.pop()

    def embaralha(self):
        shuffle(self.baralho)

    def __len__(self):  # retorna o tamanho do baralho
        return len(self.baralho)

    def __repr__(self):  # retorna a representação de string canônica
        return 'Baralho ({})'.format(self.baralho)

    def __eq__(self, outro):  # retorna True se o baralho tiver as msms carta na msm ordem
        return self.baralho == outro.baralho



