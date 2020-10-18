class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    @property #facilita o acesso ao atributo
    def nome(self): #como se fosse um getter
        print("chamando @property nome()")
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print("chamando setter nome()")
        self.__nome = nome



