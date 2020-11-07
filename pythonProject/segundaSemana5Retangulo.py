class Retangulo:

    def set_tamanho(self, coord_x, coord_y):  # construtor
        self.x = coord_x
        self.y = coord_y

    def perimetro(self):  # retorna o perimetro do retangulo
        return 2*(self.x+self.y)

    def area(self):  # retorna a area do retangulo
        return self.x*self.y