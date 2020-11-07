class Animal:  # representa um animal

    def __init__(self, especie, linguagem):
        self.ling = linguagem
        self.esp = especie

    def set_especie(self, especie):  # define especie do animal
        self.esp = especie

    def set_linguagem(self, linguagem):  # define linguagem do animal
        self.ling = linguagem

    def frase(self):  # exibe uma frase
        print('Eu sou um {} e sei {}'.format(self.esp, self.ling))