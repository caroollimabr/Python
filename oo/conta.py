#package em Python chama-se module
class Conta: #uma classe deve ter uma única responsabilidade (aqui não é para ter método "é inadimplente", por ex.

    def __init__(self, numero, titular, saldo, limite): #método/função construtora. Self é a referência/endereço do objeto
        print("Construindo objeto {}".format(self))
        self.__numero = numero # . significa "acesse"
        self.__titular = titular #__ indica private: pode ser usado apenas dentro da classe, ou seja, o atributo recebe o nome da classe como prefixo
        self.__saldo = saldo
        self.__limite = limite

    @staticmethod # método estático: USAR COM CAUTELA
    def codigo_banco(): # lembra linguagem procedural (n depende de um objeto para ser chamado e n manipula informações/atributos de objetos)
        return "341"

    @staticmethod
    def mostrar_codigos_bancos():
        return {'Itaú Unibanco': '341', 'BB': '001', 'Caixa': '104', 'Bradesco': '107'}

    @property #getter: sempre retorna algo
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter  #setter: estabelece/altera novo valor; altera o valor do atributo sem ferir o encapsulamento
    def limite(self, limite):
        self.__limite = limite

    def tira_extrato (self):
        print("Saldo de {} da(o) titular {}".format(self.__saldo, self.__titular))

    def deposita (self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar): # método private só pode ser chamado dentro da classe
        valor_disponivel = (self.__saldo + self.__limite)
        return valor_a_sacar <= valor_disponivel # retorna boolean

    def saca (self, valor):
        if(valor <= (self.__saldo + self.__limite)):
            self.__saldo -= valor
        else:
            print("Saque não realizado. O valor {} ultrapassou o limite da conta.".format(valor))

    def transfere (self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    #garbage collector: o python procura objetos que não são utilizados e jogam eles no lixo
    #se quisermos desfazer uma referência,pode-se usar None: >>> outraRef = None

#S - Single responsibility principle
#O - Open/closed principle
#L - Liskov substitution principle
#I - Interface segregation principle
#D - Dependency inversion principle