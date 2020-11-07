#representa pontos no plano
class Ponto:
    def __init__(self, coord_x = 0, coord_y = 0):
        self.x = coord_x
        self.y = coord_y
    def set_x(self, coord_x):  # define coordenada x do ponto como coord_x
        self.x = coord_x
    def set_y(self, coord_y):  # define coordenada y do ponto como coord_y
        self.y = coord_y
    def get(self):  # retorna tupla com coordenadas x e y do ponto
        return (self.x, self.y)
    def move(self, d_x, d_y):  # muda as coordenadas x e y para d_x e d_y
        self.x += d_x
        self.y += d_y
    def __eq__(self, outro):  # self == outro quando eles têm as msms coordenadas
        return self.x == outro.x and self.y == outro.y

    def __repr__(self):  # retorna representação de string canônica Ponto (x, y)
        return "Ponto ('{}', '{}')".format(self.coord_x, self.coord2_y)
        
class Vetor(Ponto):  # vetor 2d
    def __mul__(self, v):  # produto de vetores
        return self.x * v.x + self.y * v.y

    def __add__(self, v):  # adição de vetores
        return Vetor(self.x + v.x + self.y * v.y)

    def __repr__(self):  # retorna representação de string canônica
        return 'Vetor{}'.format(self.get())
