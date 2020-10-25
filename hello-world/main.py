class Ponto:
    x = 0
    y = 0

p = Ponto()
Ponto.x = 1
p.x = 2
p.y = 3
Ponto.y = 4
print(Ponto.x)
print(p.x)
print(Ponto.y)
print(p.y)

class Cachorro:
    def __init__(self, idade):
        self.idade = idade

class Dalmata(Cachorro):
    def __init__(self, idade, pedigree):
        super(Dalmata, self).__init__(idade)
        self.pedigree = pedigree

d = Dalmata(3, True)
print(d.idade, d.pedigree)